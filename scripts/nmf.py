import pandas as pd
import numpy as np
from sklearn.decomposition import NMF
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import silhouette_score
from scipy.optimize import linear_sum_assignment

def train(dataset, n_sig):
    """
    produces matrixes W and H from simulated data and fixed number of signatures
    """
    model = NMF(n_components = n_sig, init='random', random_state=None, max_iter = 4000)
    W = model.fit_transform(dataset.T)
    H = model.components_
    L = model.reconstruction_err_
    
    return W, H, L

def plot_nsig_analysis(original, rep, l, match, ax, min_signatures = 2, original_known = True):
    from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, HPacker, VPacker
    
    """
    Plots the result analysis metrics for estimated dataset given by estimate_n_signatures()
    """
    x_max = min_signatures + len(rep)
    ax.plot(np.arange(min_signatures, x_max), rep, color = "red")
    ax.plot(np.arange(min_signatures, x_max), rep, "ro")
    
    ax.plot(np.arange(min_signatures, x_max), match, "green")
    ax.plot(np.arange(min_signatures, x_max), match, "go")
    ax.set_xlim(min_signatures-1, x_max)
    ax.set_xlabel("")
    
    # fancy ylabel with colors
    ybox1 = TextArea("Reproducibility ", textprops=dict(color="r", size=10,rotation=90,ha='left',va='bottom'))
    ybox2 = TextArea("and ",     textprops=dict(color="k", size=10,rotation=90,ha='left',va='bottom'))
    ybox3 = TextArea("Dissimilarity", textprops=dict(color="g", size=10,rotation=90,ha='left',va='bottom'))
    ybox = VPacker(children=[ybox1, ybox2, ybox3],align="bottom", pad=0, sep=5)
    anchored_ybox = AnchoredOffsetbox(loc=7, child=ybox, pad=0., frameon=False, bbox_to_anchor=(-0.08, 0.5), 
                                  bbox_transform=ax.transAxes, borderpad=0.)
    ax.add_artist(anchored_ybox)
    ax.set_ylabel(None)
    
    ax2 = ax.twinx()
    ax2.plot(np.arange(min_signatures, x_max), l, color = "blue")
    ax2.plot(np.arange(min_signatures, x_max), l, "bo")
    ax2.set_ylabel('Loss (MSE/frobenius)', color = "blue")
    ax2.tick_params(axis='y', colors='blue')
    ax2.grid(visible=False)

    if original_known:
        ax.axvline(x=original.shape[0], ymin=0, color = "gray", linestyle = "--")
        ax.set_xlabel("Number of signatures", fontsize = 13)
        ax.set_title('Diagnostics for optimal number of signatures')
        #ax.set_ylabel("Reproducibility", color = "red")
        ax2.set_ylabel('Loss (MSE/frobenius)', color = "blue")


def estimate_n_signatures(dataset, n_sim = 20, min_signatures = 2, max_signatures = 10, return_avg_signatures = True):
    """
    Combines results for calculate-function for different number of n_estimates. Call this function to get stats and average signatures
    for each fixed n in 2...max_signatures
    """
    loss = []
    reproducibility = []
    signatures = []
    match = np.zeros((max_signatures - min_signatures + 1, 2))

    for sigs in range(min_signatures, max_signatures + 1): 
        if sigs%4 == 0:
            print(f"Calculating K={sigs}:")
        if return_avg_signatures:
            l, rep, sig, m = calculate(dataset, n_sim, sigs, return_avg_signatures = True)
        else:
            l, rep, sig, m = calculate(dataset, n_sim, sigs, return_avg_signatures = False)
            
        loss.append(l)
        reproducibility.append(rep)
        signatures.append(sig)
        match[(sigs - min_signatures), :] = m
    
    return np.array(loss), np.array(reproducibility), signatures, match
    
        

def calculate(dataset, n_sim, n_sigs, return_avg_signatures = True):
    """
    Given a dataset and fixed number of signatures, calculates analysis metrics for estimating the optimal number of mutational signatures. 
    Currently returns tuple of (average Silhouette, average Reconstruction loss and the average (or best) of inferred n signatures)
    """
    losses = []

    # train NMF 2 times the numer of simulations (n_sim) spesified, calculate matrics by 50% best runs
    all_signatures = np.zeros([n_sim*2, n_sigs, dataset.shape[1]])
    for sim in range(n_sim*2):
        W, H, Loss = train(dataset, n_sigs)
        losses.append(Loss)
        all_signatures[sim] = W.T

    losses = np.array(losses)
    keep = np.argsort(losses)[0:n_sim] # keep indices with lowest losses

    #return losses, keep

    all_signatures = all_signatures[keep]
    losses = losses[keep]
    Loss = np.mean(losses) # average loss is the first performance metric
    

    temp = all_signatures[np.argmin(losses), :, :]
    all_signatures[np.argmin(losses), :, :] = all_signatures[0, :, :]
    all_signatures[0, :, :] = temp

    # second best match metrics
    matches = np.sort(cosine_similarity(all_signatures[0]), axis = 1)[:, -2]
    #match_best_fit = matches.mean() # average of all sigs
    match_best_fit = np.sort(matches)[-1] # only most similar match
    
    match_avg = []
    for sigs in all_signatures:
        matches = np.sort(cosine_similarity(sigs), axis = 1)[:, -2]
        match_avg.append(np.sort(matches)[-1]) # only most similar match
    
    match = [match_best_fit, np.array(match_avg).mean()]
    
    # Use the first iteration's signatures to find best matches from latter ones
    for i in range(1, n_sim):
        sim = cosine_similarity(all_signatures[0], all_signatures[i])
        match_permutation = linear_sum_assignment(sim, maximize = True)[1] # Hungarian algorithm to find best matches
        all_signatures[i] = all_signatures[i, match_permutation, :]


    l = np.zeros([n_sigs * n_sim, dataset.shape[1]])
    for i in range(n_sigs):
        l[i * n_sim : i * n_sim + n_sim, :] = all_signatures[:, i, :]

    labels = np.repeat(np.arange(n_sigs), n_sim)
    sil_score = silhouette_score(l, labels, metric = "cosine")
 
    # return average signatures of simulations
    if return_avg_signatures:
        # Taking average of signature elements along signatures can to me intuitively be thought as an "average" of that signature
        avg_sig = np.mean(all_signatures, axis = 0)
        avg_sig = np.apply_along_axis(lambda x: x/sum(x), axis = 1, arr = avg_sig) # let's again keep the signatures scaled
        avg = pd.DataFrame(avg_sig, index = ["inferred_Signature" + str(i+1) for i in range(n_sigs)], columns = None)
        best = pd.DataFrame(all_signatures[np.argmin(losses)], index = ["inferred_Signature" + str(i+1) for i in range(n_sigs)], columns = None)
        return Loss, sil_score, best, match
    
    # else, return signature with lowest reconstruction loss
    return Loss, sil_score, temp, match
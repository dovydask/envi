import numpy as np
import pandas as pd

def simulate_species(R0, N0=0.01, n_min=2, n_max=6,
                     mu_range=(0.006, 0.02), od_range=(0.8, 1.8),
                     f_range=(0.01, 0.02), rng=np.random.default_rng(1)):
    K = len(R0)
    n = rng.integers(n_min, n_max+1)
    act = rng.choice(K, n, replace=False)
    r = np.zeros(K)
    nu = np.zeros(K)
    f = np.zeros(K)

    Nmax = rng.uniform(*od_range)
    f[act] = rng.uniform(*f_range, n)
    nu[act] = -np.log(f[act])/(Nmax - N0)

    mu = rng.uniform(*mu_range)
    w = rng.lognormal(0, 0.7, n)
    r[act] = w*mu/np.sum(w*R0[act])

    q = 10**rng.uniform(-3, -1.5)
    m = rng.uniform(0.02, 0.05)
    return r, nu, q, m, f


def dNdt(t, r, Rt, Nt, q, m, K):
    assert len(r) == len(Rt)
    return np.sum(np.array([(q/(q + np.exp(-m*t)))*r[k]*(Rt[k]/(K+Rt[k]))*Nt for k in range(len(Rt))]))


def dRdt(t, nu, Rt, Nt):
    assert len(nu) == len(Rt)
    return np.array([-nu[k]*Rt[k]*Nt for k in range(len(Rt))])

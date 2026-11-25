import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT/"data"
RESULTS_DIR = ROOT/"results"
FIGURES_DIR = RESULTS_DIR/"figures"

PSEUDOCOUNT = 0.01  # For global log operations

SPECIES_LIST = np.array([6, 105, 403, 1287, 1292, 1299, 1842, 1896, 1972, 1977, 2160, 2164, 2443, 2659, 3031, 3237])
SPECIES_LIST_WO_2164 = [str(x) for x in SPECIES_LIST if x != 2164]
SPECIES_LIST_WITH_COMM = list(SPECIES_LIST.astype(str)) + ["Comm"]

SPECIES_ORDER = ["3031", "1896", "105", "3237", "2443", "1842", "2160", "2164", "403", "2659", "1977", "6", "1287", "1292", "1299", "1972"]
SPECIES_ORDER_WO_2164 = ["3031", "1896", "105", "3237", "2443", "1842", "2160", "403", "2659", "1977", "6", "1287", "1292", "1299", "1972"]

cmap = plt.get_cmap("tab20")
colors = [cmap(i) for i in range(cmap.N)]
SPECIES_COLORS = {SPECIES_LIST_WITH_COMM[i]: colors[i] for i in range(len(SPECIES_LIST_WITH_COMM))}
SPECIES_COLORS["Comm"] = "black"
SPECIES_COLORS["3237"] = "cyan"

SPECIES_NAMES = {"6":    "Pseudomonas putida", 
                 "105":  "Agrobacterium tumefaciens", 
                 "403":  "Comamonas testosteroni", 
                 "1287": "Citrobacter koseri",
                 "1292": "Morganella morganii",
                 "1299": "Kluyvera intermedia", 
                 "1842": "Sphingobium yanoikuyae", 
                 "1896": "Sphingobacterium spiritivorum", 
                 "1972": "Aeromonas caviae",
                 "1977": "Pseudomonas chlororaphis",  
                 "2160": "Bordetella avium", 
                 "2164": "Cupriavidus necator", 
                 "2443": "Paracoccus denitrificans", 
                 "2659": "Stenotrophomonas maltophilia", 
                 "3031": "Niabella yanshanensis", 
                 "3237": "Microvirga lotononidis"}

# Includes full community and control labels for plotting purposes
SPECIES_NAMES_SHORT = {"6":    "P. putida", 
                       "105":  "A. tumefaciens", 
                       "403":  "C. testosteroni", 
                       "1287": "C. koseri", 
                       "1292": "M. morganii", 
                       "1299": "K. intermedia", 
                       "1842": "S. yanoikuyae", 
                       "1896": "S. spiritivorum", 
                       "1972": "A. caviae", 
                       "1977": "P. chlororaphis", 
                       "2160": "B. avium", 
                       "2164": "C. necator", 
                       "2443": "P. denitrificans", 
                       "2659": "S. maltophilia", 
                       "3031": "N. yanshanensis", 
                       "3237": "M. lotononidis",
                       "Comm": "Full community",
                       "Control": "Control"}

PHYLO_GROUPS = {"6":    "Gammaproteobacteria",
                  "105":  "Alphaproteobacteria",
                  "403":  "Betaproteobacteria",
                  "1287": "Gammaproteobacteria",
                  "1292": "Gammaproteobacteria",
                  "1299": "Gammaproteobacteria",
                  "1842": "Alphaproteobacteria",
                  "1896": "Bacteroidota",
                  "1972": "Gammaproteobacteria",
                  "1977": "Gammaproteobacteria",
                  "2160": "Betaproteobacteria",
                  "2164": "Betaproteobacteria",
                  "2443": "Alphaproteobacteria",
                  "2659": "Gammaproteobacteria",
                  "3031": "Bacteroidota",
                  "3237": "Alphaproteobacteria",
                  "Comm": "Full community"}

PHYLO_GROUPS_FANCY = {"6":    r"$\gamma$-proteobacteria",
                      "105":  r"$\alpha$-proteobacteria",
                      "403":  r"$\beta$-proteobacteria",
                      "1287": r"$\gamma$-proteobacteria",
                      "1292": r"$\gamma$-proteobacteria",
                      "1299": r"$\gamma$-proteobacteria",
                      "1842": r"$\alpha$-proteobacteria",
                      "1896": "Bacteroidota",
                      "1972": r"$\gamma$-proteobacteria",
                      "1977": r"$\gamma$-proteobacteria",
                      "2160": r"$\beta$-proteobacteria",
                      "2164": r"$\beta$-proteobacteria",
                      "2443": r"$\alpha$-proteobacteria",
                      "2659": r"$\gamma$-proteobacteria",
                      "3031": "Bacteroidota",
                      "3237": r"$\alpha$-proteobacteria"}

PHYLO_ORDER = [PHYLO_GROUPS[str(x)] for x in SPECIES_LIST]
PHYLO_COLORS = {"Alphaproteobacteria": "#88009d", "Bacteroidota": "#009d99", "Betaproteobacteria": "#ff0000", "Gammaproteobacteria": "#0700ff"}
PHYLO_COLORS_FANCY = {r"$\alpha$-proteobacteria": "#88009d", "Bacteroidota": "#009d99", r"$\beta$-proteobacteria": "#ff0000", r"$\gamma$-proteobacteria": "#0700ff"}

PHYLO_GROUP_COMBOS = {"Alphaproteobacteria+Alphaproteobacteria": "A+A",
                      "Alphaproteobacteria+Bacteroidota": "A+Ba",
                      "Bacteroidota+Alphaproteobacteria": "A+Ba",
                      "Alphaproteobacteria+Betaproteobacteria": "A+Be",
                      "Betaproteobacteria+Alphaproteobacteria": "A+Be",
                      "Alphaproteobacteria+Gammaproteobacteria": "A+G",
                      "Gammaproteobacteria+Alphaproteobacteria": "A+G",
                      "Bacteroidota+Bacteroidota": "Ba+Ba",
                      "Bacteroidota+Betaproteobacteria": "Ba+Be",
                      "Betaproteobacteria+Bacteroidota": "Ba+Be",
                      "Bacteroidota+Gammaproteobacteria": "Ba+G",
                      "Gammaproteobacteria+Bacteroidota": "Ba+G",
                      "Betaproteobacteria+Betaproteobacteria": "Be+Be",
                      "Betaproteobacteria+Gammaproteobacteria": "Be+G",
                      "Gammaproteobacteria+Betaproteobacteria": "Be+G",
                      "Gammaproteobacteria+Gammaproteobacteria": "G+G"}


PHYLO_GROUP_COMBO_LABELS = {"A+A": "A+A",
                            "A+Ba": "A+Ba",
                            "Ba+A": "A+Ba",
                            "A+Be": "A+Be",
                            "Be+A": "A+Be",
                            "A+G": "A+G",
                            "G+A": "A+G",
                            "Ba+Ba": "Ba+Ba",
                            "Ba+Be": "Ba+Be",
                            "Be+Ba": "Ba+Be",
                            "Ba+G": "Ba+G",
                            "G+Ba": "Ba+G",
                            "Be+Be": "Be+Be",
                            "Be+G": "Be+G",
                            "G+Be": "Be+G",
                            "G+G": "G+G"}
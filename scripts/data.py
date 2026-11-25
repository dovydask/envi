import numpy as np
import pandas as pd

from .config import *
from .utils import original_datetime_converter, smoothen

# ---------------------------------------------------------------------------
# Spent medium growth data
# ---------------------------------------------------------------------------

# Raw data
p1_1_meta = pd.read_excel(DATA_DIR/"Filtrate/1.xlsx", sheet_name="Plate 1 - Results", header=1).set_index("Well")
p1_1_data = pd.read_excel(DATA_DIR/"Filtrate/1.xlsx", sheet_name="Plate 1 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p2_1_meta = pd.read_excel(DATA_DIR/"Filtrate/1.xlsx", sheet_name="Plate 2 - Results", header=1).set_index("Well")
p2_1_data = pd.read_excel(DATA_DIR/"Filtrate/1.xlsx", sheet_name="Plate 2 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p3_1_meta = pd.read_excel(DATA_DIR/"Filtrate/1.xlsx", sheet_name="Plate 3 - Results", header=1).set_index("Well")
p3_1_data = pd.read_excel(DATA_DIR/"Filtrate/1.xlsx", sheet_name="Plate 3 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p4_1_meta = pd.read_excel(DATA_DIR/"Filtrate/1.xlsx", sheet_name="Plate 4 - Results", header=1).set_index("Well")
p4_1_data = pd.read_excel(DATA_DIR/"Filtrate/1.xlsx", sheet_name="Plate 4 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p1_2_meta = pd.read_excel(DATA_DIR/"Filtrate/2.xlsx", sheet_name="Plate 1 - Results", header=1).set_index("Well")
p1_2_data = pd.read_excel(DATA_DIR/"Filtrate/2.xlsx", sheet_name="Plate 1 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p2_2_meta = pd.read_excel(DATA_DIR/"Filtrate/2.xlsx", sheet_name="Plate 2 - Results", header=1).set_index("Well")
p2_2_data = pd.read_excel(DATA_DIR/"Filtrate/2.xlsx", sheet_name="Plate 2 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p3_2_meta = pd.read_excel(DATA_DIR/"Filtrate/2.xlsx", sheet_name="Plate 3 - Results", header=1).set_index("Well")
p3_2_data = pd.read_excel(DATA_DIR/"Filtrate/2.xlsx", sheet_name="Plate 3 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p4_2_meta = pd.read_excel(DATA_DIR/"Filtrate/2.xlsx", sheet_name="Plate 4 - Results", header=1).set_index("Well")
p4_2_data = pd.read_excel(DATA_DIR/"Filtrate/2.xlsx", sheet_name="Plate 4 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p1_3_meta = pd.read_excel(DATA_DIR/"Filtrate/3.xlsx", sheet_name="Plate 1 - Results", header=1).set_index("Well")
p1_3_data = pd.read_excel(DATA_DIR/"Filtrate/3.xlsx", sheet_name="Plate 1 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p2_3_meta = pd.read_excel(DATA_DIR/"Filtrate/3.xlsx", sheet_name="Plate 2 - Results", header=1).set_index("Well")
p2_3_data = pd.read_excel(DATA_DIR/"Filtrate/3.xlsx", sheet_name="Plate 2 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p3_3_meta = pd.read_excel(DATA_DIR/"Filtrate/3.xlsx", sheet_name="Plate 3 - Results", header=1).set_index("Well")
p3_3_data = pd.read_excel(DATA_DIR/"Filtrate/3.xlsx", sheet_name="Plate 3 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p4_3_meta = pd.read_excel(DATA_DIR/"Filtrate/3.xlsx", sheet_name="Plate 4 - Results", header=1).set_index("Well")
p4_3_data = pd.read_excel(DATA_DIR/"Filtrate/3.xlsx", sheet_name="Plate 4 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p1_4_meta = pd.read_excel(DATA_DIR/"Filtrate/4.xlsx", sheet_name="Plate 1 - Results", header=1).set_index("Well")
p1_4_data = pd.read_excel(DATA_DIR/"Filtrate/4.xlsx", sheet_name="Plate 1 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p2_4_meta = pd.read_excel(DATA_DIR/"Filtrate/4.xlsx", sheet_name="Plate 2 - Results", header=1).set_index("Well")
p2_4_data = pd.read_excel(DATA_DIR/"Filtrate/4.xlsx", sheet_name="Plate 2 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p3_4_meta = pd.read_excel(DATA_DIR/"Filtrate/4.xlsx", sheet_name="Plate 3 - Results", header=1).set_index("Well")
p3_4_data = pd.read_excel(DATA_DIR/"Filtrate/4.xlsx", sheet_name="Plate 3 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

p4_4_meta = pd.read_excel(DATA_DIR/"Filtrate/4.xlsx", sheet_name="Plate 4 - Results", header=1).set_index("Well")
p4_4_data = pd.read_excel(DATA_DIR/"Filtrate/4.xlsx", sheet_name="Plate 4 - Raw Data", header=1, 
                          converters={"Time": original_datetime_converter})

time_plates = {"t1": [(p1_2_meta, p1_2_data), (p2_2_meta, p2_2_data), (p3_2_meta, p3_2_data)],
               "t2": [(p4_2_meta, p4_2_data), (p1_3_meta, p1_3_data), (p2_3_meta, p2_3_data)],
               "t3": [(p3_3_meta, p3_3_data), (p4_3_meta, p4_3_data), (p1_4_meta, p1_4_data)],
               "t4": [(p2_4_meta, p2_4_data), (p3_4_meta, p3_4_data), (p4_4_meta, p4_4_data)]}

filtrate_growth_curves = pd.DataFrame(columns=(range(289)))
for tp in ["t1", "t2", "t3", "t4"]:
    for time_plate in time_plates[tp]:
        meta_data = time_plate[0]
        raw_data = time_plate[1]

        meta_data = meta_data[~meta_data["filtrate"].isin(["R2A", "comm"])]
        for first_species in meta_data["filtrate"].unique():
            for second_species in meta_data["species"].unique():
                wells = meta_data[(meta_data["filtrate"] == first_species) & (meta_data["species"] == second_species) \
                        & (meta_data["time point"] == int(tp[1]))]
                if len(wells) == 1:
                    well = wells.index[0]
                    filtrate_growth_curves.loc[str(first_species) + "_" + str(second_species) + "_" + tp] = raw_data.loc[:, well]
                elif len(wells) == 2 and first_species == 1972:
                    well = wells.index[0]
                    filtrate_growth_curves.loc[str(first_species) + "_" + str(second_species) + "_" + tp] = raw_data.loc[:, well]


# Monoculture growth median curves
monogrowth_medians_df = pd.DataFrame(index=p3_1_meta["species"].unique(), columns=p3_1_data.index)
for species in p3_1_meta["species"].unique():
    species_reps_df = p3_1_data.loc[:, p3_1_meta[p3_1_meta["species"] == species].index].T
    monogrowth_medians_df.loc[species] = np.median(species_reps_df, axis=0)


# Yields-only, base-corrected
species = list(pd.read_csv(DATA_DIR/"Filtrate/speciesList.csv", header=None).iloc[:, 0].to_numpy())
flt_1 = pd.read_csv(DATA_DIR/"Filtrate/filtrateY.timeIndex.1.csv", names=species)
flt_1["Species"] = species
flt_1 = flt_1.set_index("Species").T
flt_1 = flt_1.drop(2164)
flt_1 = flt_1.drop(2164, axis=1)
flt_1 -= 0.1

flt_2 = pd.read_csv(DATA_DIR/"Filtrate/filtrateY.timeIndex.2.csv", names=species)
flt_2["Species"] = species
flt_2 = flt_2.set_index("Species").T
flt_2 = flt_2.drop(2164)
flt_2 = flt_2.drop(2164, axis=1)
flt_2 -= 0.1

flt_3 = pd.read_csv(DATA_DIR/"Filtrate/filtrateY.timeIndex.3.csv", names=species)
flt_3["Species"] = species
flt_3 = flt_3.set_index("Species").T
flt_3 = flt_3.drop(2164)
flt_3 = flt_3.drop(2164, axis=1)
flt_3 -= 0.1

flt_4 = pd.read_csv(DATA_DIR/"Filtrate/filtrateY.timeIndex.4.csv", names=species)
flt_4["Species"] = species
flt_4 = flt_4.set_index("Species").T
flt_4 = flt_4.drop(2164)
flt_4 = flt_4.drop(2164, axis=1)
flt_4 -= 0.1

flt = pd.concat([flt_1, flt_2, flt_3, flt_4], axis=1)

# Filtrate with 2164, ordered using final order (for Figure S5)
flt_1_w_2164 = pd.read_csv(DATA_DIR/"Filtrate/filtrateY.timeIndex.1.csv", names=species)
flt_1_w_2164["Species"] = species
flt_1_w_2164 = flt_1_w_2164.set_index("Species").T
flt_1_w_2164 -= 0.1
flt_1_w_2164 = flt_1_w_2164.loc[np.array(SPECIES_ORDER).astype(int), np.array(SPECIES_ORDER).astype(int)]

flt_2_w_2164 = pd.read_csv(DATA_DIR/"Filtrate/filtrateY.timeIndex.2.csv", names=species)
flt_2_w_2164["Species"] = species
flt_2_w_2164 = flt_2_w_2164.set_index("Species").T
flt_2_w_2164 -= 0.1
flt_2_w_2164 = flt_2_w_2164.loc[np.array(SPECIES_ORDER).astype(int), np.array(SPECIES_ORDER).astype(int)]

flt_3_w_2164 = pd.read_csv(DATA_DIR/"Filtrate/filtrateY.timeIndex.3.csv", names=species)
flt_3_w_2164["Species"] = species
flt_3_w_2164 = flt_3_w_2164.set_index("Species").T
flt_3_w_2164 -= 0.1
flt_3_w_2164 = flt_3_w_2164.loc[np.array(SPECIES_ORDER).astype(int), np.array(SPECIES_ORDER).astype(int)]

flt_4_w_2164 = pd.read_csv(DATA_DIR/"Filtrate/filtrateY.timeIndex.4.csv", names=species)
flt_4_w_2164["Species"] = species
flt_4_w_2164 = flt_4_w_2164.set_index("Species").T
flt_4_w_2164 -= 0.1
flt_4_w_2164 = flt_4_w_2164.loc[np.array(SPECIES_ORDER).astype(int), np.array(SPECIES_ORDER).astype(int)]

flt_w_2164 = pd.concat([flt_1_w_2164, flt_2_w_2164, flt_3_w_2164, flt_4_w_2164], axis=1)


# Normalized by base-corrected monoculture growth median
flt_1_norm = flt_1.copy()
for column in flt_1_norm.columns:
    flt_1_norm.loc[:, column] /= monogrowth_medians_df.loc[column].iloc[-1] - 0.1

flt_2_norm = flt_2.copy()
for column in flt_2_norm.columns:
    flt_2_norm.loc[:, column] /= monogrowth_medians_df.loc[column].iloc[-1] - 0.1

flt_3_norm = flt_3.copy()
for column in flt_3_norm.columns:
    flt_3_norm.loc[:, column] /= monogrowth_medians_df.loc[column].iloc[-1] - 0.1

flt_4_norm = flt_4.copy()
for column in flt_4_norm.columns:
    flt_4_norm.loc[:, column] /= monogrowth_medians_df.loc[column].iloc[-1] - 0.1

flt_norm = pd.concat([flt_1_norm, flt_2_norm, flt_3_norm, flt_4_norm], axis=1)


plate_metadata = pd.read_excel(DATA_DIR/"Filtrate/1.xlsx", sheet_name="Plate 3 - Results", header=1)
plate_raw_data = pd.read_excel(DATA_DIR/"Filtrate/1.xlsx", sheet_name="Plate 3 - Raw Data", header=1)

chosen_wells = [s + i for i in ["11", "12"] for s in ["A", "B", "C", "D", "E", "F", "G", "H"]]

plate_metadata_2 = pd.read_excel(DATA_DIR/"Filtrate/2.xlsx", sheet_name="Plate 3 - Results", header=1)
plate_metadata_2 = plate_metadata_2[plate_metadata_2["Well"].isin(chosen_wells)]
plate_raw_data_2 = pd.read_excel(DATA_DIR/"Filtrate/2.xlsx", sheet_name="Plate 3 - Raw Data", header=1)

plate_metadata_3 = pd.read_excel(DATA_DIR/"Filtrate/3.xlsx", sheet_name="Plate 2 - Results", header=1)
plate_metadata_3 = plate_metadata_3[plate_metadata_3["Well"].isin(chosen_wells)]
plate_raw_data_3 = pd.read_excel(DATA_DIR/"Filtrate/3.xlsx", sheet_name="Plate 2 - Raw Data", header=1)

plate_metadata_4 = pd.read_excel(DATA_DIR/"Filtrate/4.xlsx", sheet_name="Plate 1 - Results", header=1)
plate_metadata_4 = plate_metadata_4[plate_metadata_4["Well"].isin(chosen_wells)]
plate_raw_data_4 = pd.read_excel(DATA_DIR/"Filtrate/4.xlsx", sheet_name="Plate 1 - Raw Data", header=1)

plate_metadata_5 = pd.read_excel(DATA_DIR/"Filtrate/4.xlsx", sheet_name="Plate 4 - Results", header=1)
plate_metadata_5 = plate_metadata_5[plate_metadata_5["Well"].isin(chosen_wells)]
plate_raw_data_5 = pd.read_excel(DATA_DIR/"Filtrate/4.xlsx", sheet_name="Plate 4 - Raw Data", header=1)

file_1_plate_1_meta = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_1-4_15-maalis-2024 00-50-38.xlsx", 
                                    sheet_name="Plate 1 - Results", skiprows=1).set_index("Name")
file_1_plate_2_meta = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_1-4_15-maalis-2024 00-50-38.xlsx", 
                                    sheet_name="Plate 2 - Results", skiprows=1).set_index("Name")
file_1_plate_3_meta = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_1-4_15-maalis-2024 00-50-38.xlsx", 
                                    sheet_name="Plate 3 - Results", skiprows=1).set_index("Name")
file_1_plate_4_meta = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_1-4_15-maalis-2024 00-50-38.xlsx", 
                                    sheet_name="Plate 4 - Results", skiprows=1).set_index("Name")

file_1_plate_1_raw = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_1-4_15-maalis-2024 00-50-38.xlsx", 
                                   sheet_name="Plate 1 - Raw Data", skiprows=1).drop("Time", axis=1)
file_1_plate_2_raw = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_1-4_15-maalis-2024 00-50-38.xlsx", 
                                   sheet_name="Plate 2 - Raw Data", skiprows=1).drop("Time", axis=1)
file_1_plate_3_raw = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_1-4_15-maalis-2024 00-50-38.xlsx", 
                                   sheet_name="Plate 3 - Raw Data", skiprows=1).drop("Time", axis=1)
file_1_plate_4_raw = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_1-4_15-maalis-2024 00-50-38.xlsx", 
                                   sheet_name="Plate 4 - Raw Data", skiprows=1).drop("Time", axis=1)

file_2_plate_1_meta = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_5-8_15-maalis-2024 00-50-19.xlsx", 
                                    sheet_name="Plate 1 - Results", skiprows=1).set_index("Name")
file_2_plate_2_meta = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_5-8_15-maalis-2024 00-50-19.xlsx", 
                                    sheet_name="Plate 2 - Results", skiprows=1).set_index("Name")
file_2_plate_3_meta = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_5-8_15-maalis-2024 00-50-19.xlsx", 
                                    sheet_name="Plate 3 - Results", skiprows=1).set_index("Name")
file_2_plate_4_meta = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_5-8_15-maalis-2024 00-50-19.xlsx", 
                                    sheet_name="Plate 4 - Results", skiprows=1)
file_2_plate_4_meta = file_2_plate_4_meta[~pd.isna(file_2_plate_4_meta["Name"])].set_index("Name")

file_2_plate_1_raw = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_5-8_15-maalis-2024 00-50-19.xlsx", 
                                   sheet_name="Plate 1 - Raw Data", skiprows=1).drop("Time", axis=1)
file_2_plate_2_raw = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_5-8_15-maalis-2024 00-50-19.xlsx", 
                                   sheet_name="Plate 2 - Raw Data", skiprows=1).drop("Time", axis=1)
file_2_plate_3_raw = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_5-8_15-maalis-2024 00-50-19.xlsx", 
                                   sheet_name="Plate 3 - Raw Data", skiprows=1).drop("Time", axis=1)
file_2_plate_4_raw = pd.read_excel(DATA_DIR/"OD/NMR-logphase/NMR_2024_Endpoint_5-8_15-maalis-2024 00-50-19.xlsx", 
                                   sheet_name="Plate 4 - Raw Data", skiprows=1).drop("Time", axis=1)

file_1_plate_1_meta["Plate"] = ["1"]*len(file_1_plate_1_meta)
file_1_plate_2_meta["Plate"] = ["2"]*len(file_1_plate_2_meta)
file_1_plate_3_meta["Plate"] = ["3"]*len(file_1_plate_3_meta)
file_1_plate_4_meta["Plate"] = ["4"]*len(file_1_plate_4_meta)

file_2_plate_1_meta["Plate"] = ["5"]*len(file_2_plate_1_meta)
file_2_plate_2_meta["Plate"] = ["6"]*len(file_2_plate_2_meta)
file_2_plate_3_meta["Plate"] = ["7"]*len(file_2_plate_3_meta)
file_2_plate_4_meta["Plate"] = ["8"]*len(file_2_plate_4_meta)

list_0 = list(file_1_plate_1_raw.columns)
list_1 = ["1"]*len(list_0)
list_2 = ["2"]*len(list_0)
list_3 = ["3"]*len(list_0)
list_4 = ["4"]*len(list_0)
list_5 = ["5"]*len(list_0)
list_6 = ["6"]*len(list_0)
list_7 = ["7"]*len(list_0)
list_8 = ["8"]*len(list_0)

list_lvl_1 = list_1 + list_2 + list_3 + list_4 + list_5 + list_6 + list_7 + list_8
list_lvl_2 = list_0*8
arrays = [list_lvl_1, list_lvl_2]
tuples = list(zip(*arrays))
columns = pd.MultiIndex.from_tuples(tuples)

logphase_raw_data = pd.DataFrame(pd.concat([file_1_plate_1_raw, file_1_plate_2_raw, file_1_plate_3_raw, file_1_plate_4_raw, 
                                            file_2_plate_1_raw, file_2_plate_2_raw, file_2_plate_3_raw, file_2_plate_4_raw], axis=1).to_numpy(), columns=columns)
logphase_metadata = pd.concat([file_1_plate_1_meta, file_1_plate_2_meta, file_1_plate_3_meta, file_1_plate_4_meta,
                               file_2_plate_1_meta, file_2_plate_2_meta, file_2_plate_3_meta, file_2_plate_4_meta])


# Monoculture growth curves
mono_metadata = logphase_metadata[logphase_metadata["Community type"] == "Single"]
mono_curves = pd.DataFrame(index=mono_metadata.index, columns=range(logphase_raw_data.shape[0]))
for idx in mono_curves.index:
    info = logphase_metadata.loc[idx]
    well = info["Well"]
    plate = info["Plate"]
    curve = logphase_raw_data.loc[:, (plate, well)]
    mono_curves.loc[idx] = curve

# Monoculture median curves
mono_median_curves = pd.DataFrame(columns=range(logphase_raw_data.shape[0]))
for comm in mono_metadata["Community"].unique():
    comm_df = mono_metadata[mono_metadata["Community"] == comm]
    for replicate in comm_df["Replicate"].unique():
        rep_comm_df = comm_df[comm_df["Replicate"] == replicate]
        assert len(rep_comm_df) == 2 and len(rep_comm_df["Plate"].unique()) == 1
        lr_a = rep_comm_df[rep_comm_df["Logphase replicate"] == "a"]
        lr_b = rep_comm_df[rep_comm_df["Logphase replicate"] == "b"]
        
        c_1 = logphase_raw_data.loc[:, (lr_a["Plate"].values[0], lr_a["Well"].values[0])]
        c_2 = logphase_raw_data.loc[:, (lr_b["Plate"].values[0], lr_b["Well"].values[0])]

        median_curve = np.median(np.vstack([c_1.to_numpy(), c_2.to_numpy()]), axis=0)
        mono_median_curves.loc[str(comm) + "_r" + str(int(replicate))] = median_curve


# Pairwise growth curves
pairwise_metadata = logphase_metadata[logphase_metadata["Community type"] == "Pairwise"]
pairwise_curves = pd.DataFrame(index=pairwise_metadata.index, columns=range(logphase_raw_data.shape[0]))
for idx in pairwise_curves.index:
    info = logphase_metadata.loc[idx]
    well = info["Well"]
    plate = info["Plate"]
    curve = logphase_raw_data.loc[:, (plate, well)]
    pairwise_curves.loc[idx] = curve

# Pairwise median growth curves
pairwise_median_curves = pd.DataFrame(columns=range(logphase_raw_data.shape[0]))
for comm in pairwise_metadata["Community"].unique():
    comm_df = pairwise_metadata[pairwise_metadata["Community"] == comm]
    for replicate in comm_df["Replicate"].unique():
        rep_comm_df = comm_df[comm_df["Replicate"] == replicate]
        assert len(rep_comm_df) == 2 and len(rep_comm_df["Plate"].unique()) == 1
        lr_a = rep_comm_df[rep_comm_df["Logphase replicate"] == "a"]
        lr_b = rep_comm_df[rep_comm_df["Logphase replicate"] == "b"]
        
        c_1 = logphase_raw_data.loc[:, (lr_a["Plate"].values[0], lr_a["Well"].values[0])]
        c_2 = logphase_raw_data.loc[:, (lr_b["Plate"].values[0], lr_b["Well"].values[0])]

        median_curve = np.median(np.vstack([c_1.to_numpy(), c_2.to_numpy()]), axis=0)
        pairwise_median_curves.loc[comm + "_r" + str(int(replicate))] = median_curve

# ---------------------------------------------------------------------------
# Growth curve stats
# ---------------------------------------------------------------------------

smoothening_window_curve = 15
smoothening_window_rho = 15

mono_stats_and_params = pd.DataFrame(columns=["Culture", "Species", "N0", "Mean OD", "Median OD", "AUC", "Yield", "rho_max", "t_rho_max"])
pair_stats_and_params = pd.DataFrame(columns=["Culture", "Species", "N0", "Mean OD", "Median OD", "AUC", "Yield", "rho_max", "t_rho_max"])
smooth_mono_median_curves = pd.DataFrame(columns=range(275))
smooth_pair_median_curves = pd.DataFrame(columns=range(275))

for idx in mono_median_curves.index:
    curve = mono_median_curves.loc[idx].to_numpy()
    
    Nt = smoothen(curve, smoothening_window_curve)
    dNdt = Nt[1:] - Nt[:-1]
    rho = dNdt / Nt[:-1]
    rho = smoothen(rho, smoothening_window_rho)
    smooth_mono_median_curves.loc[idx] = Nt

    mono_stats_and_params.loc[idx, "Culture"] = "Monoculture"
    mono_stats_and_params.loc[idx, "Species"] = idx.split("_")[0]
    mono_stats_and_params.loc[idx, "N0"] = Nt[0]
    mono_stats_and_params.loc[idx, "Mean OD"] = Nt.mean()
    mono_stats_and_params.loc[idx, "Mean OD"] = Nt.mean()
    mono_stats_and_params.loc[idx, "Median OD"] = np.median(Nt)
    mono_stats_and_params.loc[idx, "AUC"] = Nt.sum()
    mono_stats_and_params.loc[idx, "Yield"] = Nt[-1]
    mono_stats_and_params.loc[idx, "rho_max"] = np.max(rho)
    mono_stats_and_params.loc[idx, "t_rho_max"] = np.where(rho == np.max(rho))[0][0]

for idx in pairwise_median_curves.index:
    curve = pairwise_median_curves.loc[idx].to_numpy()

    Nt = smoothen(curve, smoothening_window_curve)
    dNdt = Nt[1:] - Nt[:-1]
    rho = dNdt / Nt[:-1]
    rho = smoothen(rho, smoothening_window_rho)

    smooth_pair_median_curves.loc[idx] = Nt
    
    pair_stats_and_params.loc[idx, "Culture"] = "Biculture"
    pair_stats_and_params.loc[idx, "Species"] = idx.split("_")[0]
    pair_stats_and_params.loc[idx, "N0"] = Nt[0]
    pair_stats_and_params.loc[idx, "Mean OD"] = Nt.mean()
    pair_stats_and_params.loc[idx, "Mean OD"] = Nt.mean()
    pair_stats_and_params.loc[idx, "Median OD"] = np.median(Nt)
    pair_stats_and_params.loc[idx, "AUC"] = Nt.sum()
    pair_stats_and_params.loc[idx, "Yield"] = Nt[-1]
    pair_stats_and_params.loc[idx, "rho_max"] = np.max(rho)
    pair_stats_and_params.loc[idx, "t_rho_max"] = np.where(rho == np.max(rho))[0][0]

mono_and_pair_stats_and_params = pd.concat([mono_stats_and_params, pair_stats_and_params])

# ---------------------------------------------------------------------------
# Time series and endpoint NMR
# ---------------------------------------------------------------------------

raw_table = pd.read_csv(DATA_DIR/"NMR/nmr-raw/VM_2024_raw_all_bucket_table.csv.csv", sep=";", index_col=0)
time_series_sample_sheet = pd.read_excel(DATA_DIR/"NMR/nmr-raw/Sample sheet NMR2024 time series.xlsx").set_index("Seq no")
time_series_sample_sheet.columns.values[-1] = "Control contents"
endpoint_sample_sheet = pd.read_excel(DATA_DIR/"NMR/nmr-raw/Sample sheet NMR2024_endpoint.xlsx", 
                                      skiprows=1).iloc[:, 1:].set_index("Seq no")

nmr_metadata = pd.DataFrame(index=raw_table.index, data={"Sequence": [int(idx.split("_")[3]) for idx in raw_table.index]})
nmr_metadata = nmr_metadata.reset_index()
nmr_metadata.columns = ["Raw index", "Seq no"]
nmr_metadata = nmr_metadata.set_index("Seq no")

time_series_seqs = list(range(1, 272))
endpoint_seqs = list(range(301, 673))
control_r2a_time_series_seqs = [293, 294, 295, 296]
control_r2a_endpoint_seqs = [673, 674, 675, 676, 677, 678, 679, 680, 681, 682]
chosen_seqs = np.array(list(time_series_seqs) + list(endpoint_seqs) + list(control_r2a_time_series_seqs) \
                       + list(control_r2a_endpoint_seqs))

time_series_indices = nmr_metadata[nmr_metadata.index.isin(time_series_seqs)]["Raw index"].values
endpoint_indices = nmr_metadata[nmr_metadata.index.isin(endpoint_seqs)]["Raw index"].values
control_r2a_time_series_indices = nmr_metadata[nmr_metadata.index.isin(control_r2a_time_series_seqs)]["Raw index"].values
control_r2a_endpoint_indices = nmr_metadata[nmr_metadata.index.isin(control_r2a_endpoint_seqs)]["Raw index"].values
chosen_indices = np.array(list(time_series_indices) + list(endpoint_indices) + list(control_r2a_time_series_indices) \
                          + list(control_r2a_endpoint_indices))

labels = list((time_series_sample_sheet.loc[np.array(time_series_seqs)]["Community"].astype(str) + "_r" + time_series_sample_sheet.loc[np.array(time_series_seqs)]["Replicate"].astype(str) + "_t" + time_series_sample_sheet.loc[np.array(time_series_seqs)]["Time point"].astype(int).astype(str)).values) \
         + list((endpoint_sample_sheet.loc[np.array(endpoint_seqs)]["Community"].astype(str) + "_r" + endpoint_sample_sheet.loc[np.array(endpoint_seqs)]["Replicate"].astype(str)).values) \
         + list((time_series_sample_sheet.loc[np.array(control_r2a_time_series_seqs)]["Community"].astype(str) + "_r" + time_series_sample_sheet.loc[np.array(control_r2a_time_series_seqs)]["Replicate"].astype(str)).values) \
         + ["Cont_r" + str(i) for i in range(1, len(control_r2a_endpoint_seqs)+1)]

metadata_df = pd.DataFrame(data={"ID": chosen_indices, "Label": labels})

ppms = np.array(raw_table.columns).astype(float)

t1_seqs = np.array(time_series_sample_sheet[time_series_sample_sheet["Time point"] == 1].index)-1
t2_seqs = np.array(time_series_sample_sheet[time_series_sample_sheet["Time point"] == 2].index)-1
t3_seqs = np.array(time_series_sample_sheet[time_series_sample_sheet["Time point"] == 3].index)-1
t4_seqs = np.array(time_series_sample_sheet[time_series_sample_sheet["Time point"] == 4].index)-1

endpoint_labels = list((endpoint_sample_sheet.loc[np.array(endpoint_seqs)]["Community"].astype(str) + "_r" + endpoint_sample_sheet.loc[np.array(endpoint_seqs)]["Replicate"].astype(str)).values)
time_series_species_labels = (time_series_sample_sheet[time_series_sample_sheet["Time point"] == 1]["Community"].astype(str) + "_r" + time_series_sample_sheet[time_series_sample_sheet["Time point"] == 1]["Replicate"].astype(str)).values

metadata_df = pd.DataFrame(data={"ID": chosen_indices, "Source": None, "Experiment": None, "Species": None, "Replicate": None, "Time point": None}, index=labels)
for label in metadata_df.index:
    a = label.split("_")
    if len(a) == 2:
        species = a[0]
        replicate = int(a[1][1:])
        timepoint = np.nan
        source = "Endpoint"
        if species == "Cont6":
            source = "Time series"
            species = np.nan
            experiment = "Control"
        elif species == "Cont":
            species = np.nan
            experiment = "Control"
        elif species == "Comm":
            experiment = "Community"
            species = "All"
        elif "+" in species:
            experiment = "Pairwise"
        elif "-" in species:
            experiment = "Leave-one-out"
            species = species.replace("Comm", "All")
        else:
            experiment = "Single species"

    elif len(a) == 3:
        species = a[0]
        replicate = int(a[1][1:])
        timepoint = int(a[2][1:])
        source = "Time series"

        if species == "Comm":
            experiment = "Community"
            species = "All"
        else:
            experiment = "Single species"

    metadata_df.loc[label, "Source"] = source
    metadata_df.loc[label, "Experiment"] = experiment
    metadata_df.loc[label, "Species"] = species
    metadata_df.loc[label, "Replicate"] = replicate
    metadata_df.loc[label, "Time point"] = timepoint

metadata_df["Label"] = metadata_df.index
metadata_df = metadata_df.set_index("ID")

# ---------------------------------------------------------------------------
# NMF data
# ---------------------------------------------------------------------------

nmr_metadata_2 = pd.read_csv(DATA_DIR/"NMR/NMF/NMR_sample_sub.csv", index_col=5)
nmr_signatures_8 = pd.read_csv(DATA_DIR/"NMR/NMF/nmr_signatures_8.csv", index_col=0)
nmr_signatures_12 = pd.read_csv(DATA_DIR/"NMR/NMF/nmr_signatures_12.csv", index_col=0)
nmr_signatures_20 = pd.read_csv(DATA_DIR/"NMR/NMF/nmr_signatures_20.csv", index_col=0)
nmr_activities_8 = pd.read_csv(DATA_DIR/"NMR/NMF/nmr_activities_8.csv", index_col=0)
nmr_activities_12 = pd.read_csv(DATA_DIR/"NMR/NMF/nmr_activities_12.csv", index_col=0)
nmr_activities_20 = pd.read_csv(DATA_DIR/"NMR/NMF/nmr_activities_20.csv", index_col=0)

nmr_signatures_8.index = [x[1:] for x in nmr_signatures_8.index]
nmr_signatures_12.index = [x[1:] for x in nmr_signatures_12.index]
nmr_signatures_20.index = [x[1:] for x in nmr_signatures_20.index]

nmf_meta = nmr_metadata_2
nmf_acts = nmr_activities_8

# Time series data
ts_nmf_control_ids = ["Cont6_r1", "Cont6_r2", "Cont6_r3", "Cont6_r4"]
ts_nmf_control_median = nmf_acts.loc[ts_nmf_control_ids].median()
ts_nmf_control_median[ts_nmf_control_median < 0] = 0
ts_nmf_control_median_ps = ts_nmf_control_median + PSEUDOCOUNT

ts_nmf_control_mean = nmf_acts.loc[ts_nmf_control_ids].mean()
ts_nmf_control_mean[ts_nmf_control_mean < 0] = 0
ts_nmf_control_mean_ps = ts_nmf_control_mean + PSEUDOCOUNT

ts_nmf_ids = nmr_metadata_2[(nmr_metadata_2["Time point"].isin(["1", "2", "3", "4"]))].index
ts_nmf_bc_acts = pd.DataFrame(columns=nmf_acts.columns)
ts_nmf_nbc_acts = pd.DataFrame(columns=nmf_acts.columns)
ts_nmf_impacts = pd.DataFrame(columns=nmf_acts.columns)

for idx in ts_nmf_ids:
    acts = nmf_acts.loc[idx].copy()
    acts[acts < 0] = 0
    acts += PSEUDOCOUNT
    ts_nmf_bc_acts.loc[idx] = acts/ts_nmf_control_median_ps
    ts_nmf_nbc_acts.loc[idx] = acts - PSEUDOCOUNT
    ts_nmf_impacts.loc[idx] = np.log(acts + PSEUDOCOUNT) - np.log(ts_nmf_control_median_ps + PSEUDOCOUNT)

ts_nmf_mono_bc_acts = ts_nmf_bc_acts.loc[[x for x in ts_nmf_bc_acts.index if not "Comm" in x]]
ts_nmf_comm_bc_acts = ts_nmf_bc_acts.loc[[x for x in ts_nmf_bc_acts.index if "Comm" in x]]

ts_nmf_mono_nbc_acts = ts_nmf_nbc_acts.loc[[x for x in ts_nmf_nbc_acts.index if not "Comm" in x]]
ts_nmf_comm_nbc_acts = ts_nmf_nbc_acts.loc[[x for x in ts_nmf_nbc_acts.index if "Comm" in x]]

ts_nmf_mono_impacts = ts_nmf_impacts.loc[[x for x in ts_nmf_impacts.index if not "Comm" in x]]
ts_nmf_comm_impacts = ts_nmf_impacts.loc[[x for x in ts_nmf_impacts.index if "Comm" in x]]

ts_nmf_mono_bc_acts_medians = pd.DataFrame(columns=ts_nmf_mono_bc_acts.columns)
ts_nmf_mono_nbc_acts_medians = pd.DataFrame(columns=ts_nmf_mono_bc_acts.columns)
for species in SPECIES_LIST.astype(str):
    for tp in ["t1", "t2", "t3", "t4"]:
        idx = [x for x in ts_nmf_mono_bc_acts.index if x.split("_")[0] == species and x.split("_")[2] == tp]
        ts_nmf_mono_bc_acts_medians.loc[species + "_m_" + tp] = ts_nmf_mono_bc_acts.loc[idx].median(axis=0)
        ts_nmf_mono_nbc_acts_medians.loc[species + "_m_" + tp] = ts_nmf_mono_nbc_acts.loc[idx].median(axis=0)

ts_nmf_comm_bc_acts_medians = pd.DataFrame(columns=ts_nmf_comm_bc_acts.columns)
ts_nmf_comm_nbc_acts_medians = pd.DataFrame(columns=ts_nmf_comm_bc_acts.columns)
for tp in ["t1", "t2", "t3", "t4"]:
    idx = [x for x in ts_nmf_comm_bc_acts.index if x.split("_")[2] == tp]
    ts_nmf_comm_bc_acts_medians.loc["Comm_m_" + tp] = ts_nmf_comm_bc_acts.loc[idx].median(axis=0)
    ts_nmf_comm_nbc_acts_medians.loc["Comm_m_" + tp] = ts_nmf_comm_nbc_acts.loc[idx].median(axis=0)

ts_nmf_bc_acts_medians = pd.concat([ts_nmf_mono_bc_acts_medians, ts_nmf_comm_bc_acts_medians])
ts_nmf_nbc_acts_medians = pd.concat([ts_nmf_mono_nbc_acts_medians, ts_nmf_comm_nbc_acts_medians])

ts_nmf_mono_impact_medians = pd.DataFrame(columns=ts_nmf_mono_impacts.columns)
for species in SPECIES_LIST.astype(str):
    for tp in ["t1", "t2", "t3", "t4"]:
        idx = [x for x in ts_nmf_mono_impacts.index if x.split("_")[0] == species and x.split("_")[2] == tp]
        ts_nmf_mono_impact_medians.loc[species + "_m_" + tp] = ts_nmf_mono_impacts.loc[idx].median(axis=0)

ts_nmf_comm_impact_medians = pd.DataFrame(columns=ts_nmf_comm_impacts.columns)
for species in SPECIES_LIST.astype(str):
    for tp in ["t1", "t2", "t3", "t4"]:
        idx = [x for x in ts_nmf_comm_impacts.index if x.split("_")[2] == tp]
        ts_nmf_comm_impact_medians.loc["Comm_m_" + tp] = ts_nmf_comm_impacts.loc[idx].median(axis=0)

ts_nmf_impact_medians = pd.concat([ts_nmf_mono_impact_medians, ts_nmf_comm_impact_medians])

# Endpoint data
ep_nmf_control_ids = nmf_meta[nmf_meta["Community"] == "Cont"].index
ep_nmf_control_median = nmf_acts.loc[ep_nmf_control_ids].median()
ep_nmf_control_median[ep_nmf_control_median < 0] = 0

ep_nmf_control_median_ps = ep_nmf_control_median + PSEUDOCOUNT

ep_nmf_ids = nmf_meta[(nmf_meta["Time point"] == "Endpoint") & (nmf_meta["Community type"].isin(["Single", "All 16", "Pairwise", "Leave One Out"]))].index
ep_nmf_ids = [x for x in ep_nmf_ids if not "evo" in x and not "anc" in x]
ep_nmf_bc_acts = pd.DataFrame(columns=nmf_acts.columns)
ep_nmf_nbc_acts = pd.DataFrame(columns=nmf_acts.columns)
ep_nmf_impacts = pd.DataFrame(columns=nmf_acts.columns)
for idx in ep_nmf_ids:
    acts = nmf_acts.loc[idx].copy()
    acts[acts < 0] = 0
    acts += PSEUDOCOUNT
    ep_nmf_bc_acts.loc[idx] = acts/ep_nmf_control_median_ps
    ep_nmf_nbc_acts.loc[idx] = acts - PSEUDOCOUNT
    ep_nmf_impacts.loc[idx] = np.log(acts + PSEUDOCOUNT) - np.log(ep_nmf_control_median_ps + PSEUDOCOUNT)

ep_nmf_nbc_acts_medians = pd.DataFrame(columns=ep_nmf_nbc_acts.columns)
ep_nmf_bc_acts_medians = pd.DataFrame(columns=ep_nmf_bc_acts.columns)
ep_nmf_impact_medians = pd.DataFrame(columns=ep_nmf_impacts.columns)
for species in list(SPECIES_LIST.astype(str)) + ["Comm"] + ["Comm-"+x for x in SPECIES_LIST.astype(str)] + [str(SPECIES_LIST[i])+"+"+str(SPECIES_LIST[j]) for i in range(len(SPECIES_LIST)-1) for j in range(i+1, len(SPECIES_LIST))]:
    idx = [x for x in ep_nmf_bc_acts.index if x.split("_")[0] == species]
    ep_nmf_bc_acts_medians.loc[species + "_m_ep"] = ep_nmf_bc_acts.loc[idx].median(axis=0)
    ep_nmf_nbc_acts_medians.loc[species + "_m_ep"] = ep_nmf_nbc_acts.loc[idx].median(axis=0)
    ep_nmf_impact_medians.loc[species + "_m_ep"] = ep_nmf_impacts.loc[idx].median(axis=0)


interp_log_ts_df = pd.DataFrame(columns=ts_nmf_nbc_acts.columns, dtype=float)

for sp in SPECIES_LIST_WITH_COMM:
    sp_df = ts_nmf_nbc_acts.loc[[x for x in ts_nmf_nbc_acts.index if x.split("_")[0] == sp]]
    sp_df["Replicate"] = [x.split("_")[1] for x in sp_df.index]
    sp_df["Time point"] = [x.split("_")[-1] for x in sp_df.index]
    for replicate in ["r1", "r2", "r3", "r4"]:
        rep_df = sp_df[sp_df["Replicate"] == replicate].sort_values("Time point").drop(["Replicate", "Time point"], axis=1)
        sp_interp_df = pd.DataFrame(index=[f"{sp}_{replicate}_t{i}" for i in range(0, 9)], columns=rep_df.columns, dtype=float)
        sp_interp_df.loc[f"{sp}_{replicate}_t0"] = np.log(ts_nmf_control_median + PSEUDOCOUNT)
        sp_interp_df.loc[f"{sp}_{replicate}_t2"] = np.log(rep_df.loc[f"{sp}_{replicate}_t1"] + PSEUDOCOUNT)
        sp_interp_df.loc[f"{sp}_{replicate}_t4"] = np.log(rep_df.loc[f"{sp}_{replicate}_t2"] + PSEUDOCOUNT)
        sp_interp_df.loc[f"{sp}_{replicate}_t6"] = np.log(rep_df.loc[f"{sp}_{replicate}_t3"] + PSEUDOCOUNT)
        sp_interp_df.loc[f"{sp}_{replicate}_t8"] = np.log(rep_df.loc[f"{sp}_{replicate}_t4"] + PSEUDOCOUNT)
        interp_log_ts_df = pd.concat([interp_log_ts_df, sp_interp_df.interpolate(axis=0)])

# ---------------------------------------------------------------------------
# Interpolated data and impact vectors (sans dNdt) for angle calculation
# ---------------------------------------------------------------------------

interp_log_ep_df = pd.DataFrame(columns=ep_nmf_nbc_acts.columns, dtype=float)

for sp in SPECIES_LIST_WITH_COMM:
    for rep in ["r1", "r2", "r3", "r4"]:
        interp_log_ep_df.loc[f"{sp}_{rep}_ep"] = np.log(ep_nmf_nbc_acts.loc[sp + "_" + rep + "_ep"] + PSEUDOCOUNT)

for i in range(len(SPECIES_LIST)-1):
    sp1 = str(SPECIES_LIST[i])
    for j in range(i+1, len(SPECIES_LIST)):
        sp2 = str(SPECIES_LIST[j])
        for rep in ["r1", "r2"]:
            interp_log_ep_df.loc[f"{sp1}+{sp2}_{rep}_ep"] = np.log(ep_nmf_nbc_acts.loc[sp1 + "+" + sp2 + "_" + rep + "_ep"] + PSEUDOCOUNT)

interp_log_df = pd.concat([interp_log_ts_df, interp_log_ep_df])

interp_tp_to_timepoints_dict = {"t0": 0, "t1": 6*3, "t2": 6*6, "t3": 6*9, "t4": 6*12, "t5": 6*18, "t6": 6*24, "t7": 6*36, "t8": 6*48}

def nu_ts(Rt_i, tp1, tp2):
    return Rt_i.loc[tp2] - Rt_i.loc[tp1]

def nu_ep(Rt_i, R_0):
    return Rt_i - R_0

interp_nu_df = pd.DataFrame(columns=list(interp_log_df.columns) + ["Interval", "Interval (hours)"])
R_0 = np.log(ts_nmf_control_median + PSEUDOCOUNT)
for sp in SPECIES_LIST.astype(str):
    for rep in ["r1", "r2", "r3", "r4"]:
        sp_rep_df = interp_log_df.loc[[x for x in interp_log_df.index if x.split("_")[0] == sp and x.split("_")[1] == rep]]
        sp_rep_df.index = [x.split("_")[-1] for x in sp_rep_df.index]
        sp_interp_nuhat_df = pd.DataFrame(columns=interp_nu_df.columns)
        for tp_pair in [("t0", "t1"), ("t1", "t2"), ("t2", "t3"), ("t3", "t4"), ("t4", "t5"), ("t5", "t6"), ("t6", "t7"), ("t7", "t8")]:
            sp_interp_nuhat_df.loc[f"{sp}_{rep}_{tp_pair[0]}", [f"Sig {i}" for i in range(1, 9)]] = nu_ts(sp_rep_df, tp_pair[0], tp_pair[1])
            sp_interp_nuhat_df.loc[f"{sp}_{rep}_{tp_pair[0]}", "Interval"] = f"{tp_pair[0]}->{tp_pair[1]}"
            sp_interp_nuhat_df.loc[f"{sp}_{rep}_{tp_pair[0]}", "Interval (hours)"] = f"{int(interp_tp_to_timepoints_dict[tp_pair[0]]*10/60)}h->{int(interp_tp_to_timepoints_dict[tp_pair[1]]*10/60)}h"
        
        sp_interp_nuhat_df.loc[f"{sp}_{rep}_t8", [f"Sig {i}" for i in range(1, 9)]] = nu_ts(sp_rep_df, "t0", "t8")
        sp_interp_nuhat_df.loc[f"{sp}_{rep}_t8", "Interval"] = f"t0->t8"
        sp_interp_nuhat_df.loc[f"{sp}_{rep}_t8", "Interval (hours)"] = f"0h->48h"
        interp_nu_df = pd.concat([interp_nu_df, sp_interp_nuhat_df])


R_0 = np.log(ep_nmf_control_median + PSEUDOCOUNT)
for sp in SPECIES_LIST.astype(str):
    ep_nu_df = pd.DataFrame(columns=interp_log_df.columns)
    for rep in ["r1", "r2", "r3", "r4"]:
        Rt_sp = interp_log_df.loc[sp + "_" + rep + "_ep"]
        ep_nu_df.loc[f"{sp}_{rep}_ep", [f"Sig {i}" for i in range(1, 9)]] = nu_ep(Rt_sp, R_0)
        ep_nu_df.loc[f"{sp}_{rep}_ep", "Interval"] = f"t0->t8"
        ep_nu_df.loc[f"{sp}_{rep}_ep", "Interval (hours)"] = f"0h->48h"
    interp_nu_df = pd.concat([interp_nu_df, ep_nu_df])


for i in range(len(SPECIES_LIST)-1):
    sp1 = str(SPECIES_LIST[i])
    for j in range(i+1, len(SPECIES_LIST)):
        sp2 = str(SPECIES_LIST[j])
        bi_nu_df = pd.DataFrame(columns=interp_log_df.columns)
        for rep in ["r1", "r2"]:
            Rt_bi = interp_log_df.loc[sp1 + "+" + sp2 + "_" + rep + "_ep"]
            bi_nu_df.loc[f"{sp1}+{sp2}_{rep}_ep", [f"Sig {i}" for i in range(1, 9)]] = nu_ep(Rt_bi, R_0)
            bi_nu_df.loc[f"{sp1}+{sp2}_{rep}_ep", "Interval"] = f"t0->t8"
            bi_nu_df.loc[f"{sp1}+{sp2}_{rep}_ep", "Interval (hours)"] = f"0h->48h"
        
        interp_nu_df = pd.concat([interp_nu_df, bi_nu_df])
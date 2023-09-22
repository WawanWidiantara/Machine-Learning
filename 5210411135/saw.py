# %%
# kriteria = {
#     "C1": {"bobot": 0.2, "attribut": "benefit"},
#     "C2": {"bobot": 0.3, "attribut": "benefit"},
#     "C3": {"bobot": 0.15, "attribut": "cost"},
#     "C4": {"bobot": 0.35, "attribut": "benefit"},
# }

# alternatif = {
#     "A1": {"C1": "sejuk", "C2": "pacar", "C3": "30-35", "C4": "asin"},
#     "A2": {"C1": "panas", "C2": "sendiri", "C3": "30-35", "C4": "asin"},
#     "A3": {"C1": "sejuk", "C2": "keluarga", "C3": "20-25", "C4": "pedas"},
#     "A4": {"C1": "dingin", "C2": "teman", "C3": "20-25", "C4": "asin"},
#     "A5": {"C1": "panas", "C2": "sendiri", "C3": "30-35", "C4": "asin"},
#     "A6": {"C1": "dingin", "C2": "keluarga", "C3": "30-35", "C4": "manis"},
#     "A7": {"C1": "sejuk", "C2": "keluarga", "C3": "20-25", "C4": "pedas"},
#     "A8": {"C1": "panas", "C2": "teman", "C3": "20-25", "C4": "pahit"},
#     "A9": {"C1": "sejuk", "C2": "teman", "C3": "15-20", "C4": "pahit"},
#     "A10": {"C1": "sejuk", "C2": "pacar", "C3": "15-20", "C4": "manis"},
#     "A11": {"C1": "panas", "C2": "sendiri", "C3": "20-25", "C4": "manis"},
#     "A12": {"C1": "panas", "C2": "teman", "C3": "15-20", "C4": "manis"},
# }


# %%
# def addKriteria(bobot, attribut):
#     lastKeyKriteria = len(list(kriteria.keys()))
#     keyKriteria = f"C{lastKeyKriteria+1}"
#     kriteria[keyKriteria] = {"bobot": bobot, "attribut": attribut}
#     lastKeyKriteria += 1
#     print(lastKeyKriteria)

#     lastKeyAlternatif = len(list(alternatif.keys()))
#     keyAlternatif = f"C{lastKeyAlternatif+1}"
#     newAlternatif = {}
#     for i in range(lastKeyKriteria):
#         addKey = f"C{i+1}"
#         newAlternatif.update({addKey: 0})
#     alternatif[keyAlternatif] = {"bobot": bobot, "attribut": attribut}


# def bobotAlternatif(sub_kriteria, label, bobot_max, bobot_min):
#     if kriteria[label]["attribut"] == "cost":
#         bobot_min = bobot_max
#         bobot_max = 1
#     input_user = input(f"{label}: ")
#     map_kriteria = sub_kriteria.copy()
#     for key in map_kriteria.keys():
#         if key == input_user:
#             map_kriteria[key] = bobot_max
#         if key != input_user:
#             map_kriteria[key] = bobot_min
#     return map_kriteria


# %%
from copy import deepcopy
import pandas as pd
from category_encoders import OrdinalEncoder

# %%
alternatif_dict = [
    {"id_alternatif": "A1", "sub_kriteria": "sejuk, pacar, 30-35, asin"},
    {"id_alternatif": "A2", "sub_kriteria": "panas, sendiri, 30-35, asin"},
    {"id_alternatif": "A3", "sub_kriteria": "sejuk, keluarga, 20-25, pedas"},
    {"id_alternatif": "A4", "sub_kriteria": "dingin, teman, 20-25, asin"},
    {"id_alternatif": "A5", "sub_kriteria": "panas, sendiri, 30-35, asin"},
    {"id_alternatif": "A6", "sub_kriteria": "dingin, keluarga, 30-35, manis"},
    {"id_alternatif": "A7", "sub_kriteria": "sejuk, keluarga, 20-25, pedas"},
    {"id_alternatif": "A8", "sub_kriteria": "panas, teman, 20-25, pahit"},
    {"id_alternatif": "A9", "sub_kriteria": "sejuk, teman, 15-20, pahit"},
    {"id_alternatif": "A10", "sub_kriteria": "sejuk, pacar, 15-20, manis"},
    {"id_alternatif": "A11", "sub_kriteria": "panas, sendiri, 20-25, manis"},
    {"id_alternatif": "A12", "sub_kriteria": "panas, teman, 15-20, manis"},
]

alternatif_df = pd.DataFrame(alternatif_dict)
alternatif_df
# %%
kriteria_dict = [
    {"nama": "Cuaca", "bobot": 0.2, "attribut": "benefit"},
    {"nama": "Kondisi", "bobot": 0.3, "attribut": "benefit"},
    {"nama": "Budget", "bobot": 0.15, "attribut": "cost"},
    {"nama": "Rasa", "bobot": 0.35, "attribut": "benefit"},
]

kriteria_df = pd.DataFrame(kriteria_dict)
kriteria_df

# %%
sub_kriteria_dict = [
    {"kriteria": "Cuaca", "sub_kriteria": "panas"},
    {"kriteria": "Cuaca", "sub_kriteria": "sejuk"},
    {"kriteria": "Cuaca", "sub_kriteria": "dingin"},
    {"kriteria": "Kondisi", "sub_kriteria": "teman"},
    {"kriteria": "Kondisi", "sub_kriteria": "keluarga"},
    {"kriteria": "Kondisi", "sub_kriteria": "pacar"},
    {"kriteria": "Kondisi", "sub_kriteria": "sendiri"},
    {"kriteria": "Budget", "sub_kriteria": "30-35"},
    {"kriteria": "Budget", "sub_kriteria": "25-30"},
    {"kriteria": "Budget", "sub_kriteria": "20-25"},
    {"kriteria": "Budget", "sub_kriteria": "15-20"},
    {"kriteria": "Rasa", "sub_kriteria": "manis"},
    {"kriteria": "Rasa", "sub_kriteria": "asin"},
    {"kriteria": "Rasa", "sub_kriteria": "pedas"},
    {"kriteria": "Rasa", "sub_kriteria": "asam"},
    {"kriteria": "Rasa", "sub_kriteria": "pahit"},
]

sub_kriteria_df = pd.DataFrame(sub_kriteria_dict)
sub_kriteria_df

# %%
saw_dict = [
    {"alternatif": "A", "kategori": "sdfa"},
    {"alternatif": "A", "kategori": "asd"},
    {"alternatif": "A", "kategori": "sdadf"},
    {"alternatif": "B", "kategori": "sfs"},
    {"alternatif": "B", "kategori": "asdf"},
    {"alternatif": "B", "kategori": "sdfa"},
    {"alternatif": "B", "kategori": "asf"},
]

saw_df = pd.DataFrame(saw_dict)
saw_df.groupby("alternatif", as_index=False).agg({"kategori": ", ".join})


# %%
col_name = kriteria_df["nama"].values.tolist()
alternatif_df[col_name] = alternatif_df["sub_kriteria"].str.split(", ", expand=True)
data_df = alternatif_df.drop(["sub_kriteria"], axis=1).copy()

df = data_df.drop(["id_alternatif"], axis=1).copy()
df


# %%
def bobot_alternatife(sub_kriteria, label, bobot_max, bobot_min):
    selected_kriteria = kriteria_df.loc[kriteria_df["nama"] == label]
    if selected_kriteria.iloc[0]["attribut"] == "cost":
        bobot_min = bobot_max
        bobot_max = 1
    input_user = input(f"{label}: ")
    map_kriteria = sub_kriteria.copy()
    for key in map_kriteria.keys():
        if key == input_user:
            map_kriteria[key] = bobot_max
        if key != input_user:
            map_kriteria[key] = bobot_min
    return map_kriteria


def maping_subkriteria(map_dict):
    key_kriteria = sub_kriteria_df.iloc[:]["kriteria"].unique().tolist()
    for key in key_kriteria:
        map_dict[key] = {}
        selected_sub = sub_kriteria_df.loc[sub_kriteria_df["kriteria"] == key]
        val_kriteria = selected_sub.iloc[:]["sub_kriteria"].values.tolist()
        for value in val_kriteria:
            map_dict[key].update({value: 0})


def normalisasi(normalisasi):
    for key in normalisasi.keys():
        selected_kriteria = kriteria_df.loc[kriteria_df["nama"] == key]
        if selected_kriteria.iloc[0]["attribut"] != "cost":
            max_value = normalisasi[key].max()
            for i in range(normalisasi.shape[0]):
                max_norm = normalisasi[key][i] / max_value
                normalisasi.loc[i, key] = max_norm
        if selected_kriteria.iloc[0]["attribut"] == "cost":
            min_value = normalisasi[key].min()
            for i in range(normalisasi.shape[0]):
                min_norm = min_value / normalisasi[key][i]
                normalisasi.loc[i, key] = min_norm


def preferensi(preferensi):
    for key in preferensi.keys():
        selected_kriteria = kriteria_df.loc[kriteria_df["nama"] == key]
        bobot = selected_kriteria.iloc[0]["bobot"]
        for i in range(preferensi.shape[0]):
            nilai_preferensi = bobot * preferensi[key][i]
            preferensi.loc[i, key] = nilai_preferensi


def ranking(rank):
    rank["Jumlah"] = rank.sum(axis=1)
    rank["Alternatif"] = alternatif_df["id_alternatif"]


# %%
map_kriteria = {}
maping_subkriteria(map_kriteria)

key_kriteria = sub_kriteria_df.iloc[:]["kriteria"].unique().tolist()
for key in key_kriteria:
    map_kriteria[key] = {}
    selected_sub = sub_kriteria_df.loc[sub_kriteria_df["kriteria"] == key]
    val_kriteria = selected_sub.iloc[:]["sub_kriteria"].values.tolist()
    for value in val_kriteria:
        map_kriteria[key].update({value: 0})

for key in map_kriteria:
    map_kriteria[key] = bobot_alternatife(
        map_kriteria[key], key, len(list(map_kriteria[key].keys())), 1
    )

for key in df.keys():
    kriteria_num = [{"col": key, "mapping": map_kriteria[key]}]
    oe = OrdinalEncoder(mapping=kriteria_num)
    df[[key]] = oe.fit_transform(df[[key]])

print("\nHasil pembobotan")
print(df)

normalisasi_df = df.copy()
normalisasi(normalisasi_df)
print("\nHasil normalisasi")
print(normalisasi_df)

preferensi_df = normalisasi_df.copy()
preferensi(preferensi_df)
print("\nHasil Preferensi")
print(preferensi_df)

rank_df = preferensi_df.copy()
ranking(rank_df)
print("\nHasil Perankingan Urut")
print(rank_df)

sorted_rank = rank_df.sort_values(by=["Jumlah"], ascending=False)
print("\nHasil Perankingan Urut")
print(sorted_rank)

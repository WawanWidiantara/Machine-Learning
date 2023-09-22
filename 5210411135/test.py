# import math

# data = [84,88,65,77,71,50,91,82,74,78,80,65]
# hasil = []
# for i in data:
#     h = ((i - 75.42)**2)
#     hasil.append(h)

# print((sum(hasil))/11)
# print((sum(data)))

# %%
from collections import OrderedDict

kriteria = [
    "cuaca",
    "cuaca",
    "cuaca",
    "cuaca",
    "cuaca",
    "kondisi",
    "kondisi",
    "kondisi",
    "kondisi",
    "kondisi",
    "budget",
    "budget",
    "budget",
    "budget",
    "budget",
    "rasa",
    "rasa",
    "rasa",
    "rasa",
    "rasa",
    "waktu",
    None,
    None,
    None,
    None,
]

counter = max([kriteria.count(i) for i in kriteria if i != None])
set_key = []
for key in list(OrderedDict.fromkeys(kriteria)):
    if key != None:
        print(key, kriteria.count(key))
        if kriteria.count(key) == counter:
            set_key.append(key)

print(set_key, counter)

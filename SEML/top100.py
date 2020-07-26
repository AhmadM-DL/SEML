# %%

from collections import defaultdict
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
import string

# %%
top_100 = pd.read_excel("C:\\Users\\PC\\Desktop\\Interaction SE with ML\\SEML\\data\\top100.xlsx")

# %%

DL = ["AE", "GAN", "GGNN", "CNN", "RNN", "LSTM", "GRU"]
TR = ["BoW", "CART", "DT", "KNN", "RF", "LR", "SVM"]

items = []
for item in top_100["ML"].values:
    if not item == "_" and not pd.isna(item):
        items.append(item.split(","))

mixed = 0
unmixed = 0
for item_set in items:
    use_DL=False
    use_TR=False
    for item in item_set:
        if item == "RL":
            continue
        if item in DL:
            use_DL=True
        else:
            use_TR=True
    if use_TR and use_DL:
        mixed+=1
    else:
        unmixed+=1

# items = [item.strip() for item in items]

# models, counts = np.unique(items, return_counts=True)
# sorted_index = np.argsort(counts)
# counts = counts[sorted_index]
# models= models[sorted_index]

# plt.bar(models, counts)
# plt.title("Models used in SE-ML papers")
# plt.xticks(rotation=90)
# plt.xlabel("Models")
# plt.ylabel("Counts")
# %%
phases, counts = np.unique(top_100["SE cycle"].dropna(), return_counts=True)
cycle_index = [4, 0, 5, 1, 3, 2]
counts = counts[cycle_index]
phases= phases[cycle_index]

plt.bar(phases, counts)
plt.title("ML applicability in SE phases")
plt.xticks(rotation=30)
plt.yticks([0,5,10,15,20])
plt.xlabel("Phases")
plt.ylabel("Counts")

# %%
items= []
for item in top_100["languages"].dropna().values:
    items.extend(item.split(","))

items = [item.strip() for item in items]

langs, counts = np.unique(items, return_counts=True)
sorted_index = np.argsort(counts)
counts = counts[sorted_index]
langs= langs[sorted_index]

plt.bar(langs, counts)
plt.title("Languages targeted in SE-ML papers")
plt.xticks(rotation=90)
plt.xlabel("Languages")
plt.ylabel("Counts")
# %%
items= []
for item in top_100["theme"].dropna().values:
    items.append(item)

items = [item.strip() for item in items]

themes, counts = np.unique(items, return_counts=True)
sorted_index = np.argsort(counts)
counts = counts[sorted_index]
themes= themes[sorted_index]

plt.bar(themes, counts)
plt.title("Abstracted application themes in SE-ML papers")
plt.xticks(rotation=90)
plt.xlabel("Themes")
plt.ylabel("Counts")

# %%

# %%

from collections import defaultdict
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
import string

# %%

se_conf_papers_w_abstract_fp = open("softwar_eng_confs_papers_with_abst.json")
se_conf_papers_w_abstract = json.load(se_conf_papers_w_abstract_fp)
se_conf_papers_w_abstract_df = pd.DataFrame(columns=["Id", "Conference", "Year", "Title", "Authors", "Abstract"])

# %%
for conf, conf_obj in se_conf_papers_w_abstract.items():
    for year, papers in conf_obj.items():
        for paper in papers:
            se_conf_papers_w_abstract_df = se_conf_papers_w_abstract_df.append(
                {"Id": paper["id"],
                 "Title": paper["title"],
                 "Conference": conf,
                 "Year": year,
                 "Authors": ",".join(paper["authors"]),
                 "Abstract": paper["abstract"]},
                 ignore_index=True
                )

#%%
se_conf_papers_w_abstract_df = se_conf_papers_w_abstract_df.replace({"Conference": {"icse/icse": "ICSE",
                                    "icst/icst":"ICST",
                                    "sigsoft/fse":"FSE",
                                    "kbse/ase":"ASE",
                                    "issta/issta":"ISSTA",
                                    "issre/issre":"ISSRE"}})
# %%
df2 = se_conf_papers_w_abstract_df.groupby(['Conference', 'Year'])['Id'].count().unstack('Year').fillna(0)
ax= df2[['2017','2018', '2019']].plot(kind='bar', stacked=True)


#%%

ml_keywords= ["train", "training", "learning", "classify", "classifier", "cluster", "clustering", "regression", "machine", "deep", "neural", "network", "networks"]



scores = [0]*len(se_conf_papers_w_abstract_df)
for i in range(len(se_conf_papers_w_abstract_df)):
    row_ml_score=0
    for keyword in ml_keywords:
        if keyword in se_conf_papers_w_abstract_df["Title"][i] or keyword in se_conf_papers_w_abstract_df["Abstract"][i]:
            row_ml_score+=1
    scores[i]=row_ml_score

se_conf_papers_w_abstract_df["ml_score"] = scores

# %%
se_conf_papers_w_abstract_df[se_conf_papers_w_abstract_df["ml_score"] == 1].to_csv("temp.csv")

# %%
se_conf_papers_w_abstract_df.groupby(["ml_score"])["Id"].count()

# %%
se_conf_papers_w_abstract_df["ml_score"].hist()

# %%
sorted_by_ml_score = se_conf_papers_w_abstract_df.sort_values(by="ml_score", ascending=False)
sorted_by_ml_score_100 = sorted_by_ml_score.head(100)

# %%
sorted_by_ml_score_100.groupby(by="Conference").count()["Id"].plot.bar()
plt.title("Studied SE-ML papers count distribution over conferences")
plt.ylabel("Counts")


# %%

_all_ = se_conf_papers_w_abstract_df.groupby(['Conference'])['Id'].count()
_studied_ = sorted_by_ml_score_100.groupby(by="Conference")["Id"].count()

(_studied_/_all_*100).plot.bar()
plt.title("Percentage of machine learning papers in conferences")
plt.ylabel("%")

# %%
(_studied_/_all_*100).mean()


# %%

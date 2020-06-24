import pandas as pd
from collections import defaultdict
import json
import matplotlib.pyplot as plt

# se_conf_papers_w_abstract_fp = open("softwar_eng_confs_papers_with_abst.json")
# se_conf_papers_w_abstract = json.load(se_conf_papers_w_abstract_fp)
# se_conf_papers_w_abstract_df = pd.DataFrame(columns=["Id", "Conf", "Year", "Title", "Authors", "Abstract"])


# ml_keywords= ["train", "training", "learning", "classify", "classifier", "cluster", "clustering", "regression", "machine", "deep", "neural", "network", "networks"]

# for conf, conf_obj in se_conf_papers_w_abstract.items():
#     for year, papers in conf_obj.items():
#         for paper in papers:
#             se_conf_papers_w_abstract_df = se_conf_papers_w_abstract_df.append(
#                 {"Id": paper["id"],
#                  "Title": paper["title"],
#                  "Conf": conf,
#                  "Year": year,
#                  "Authors": ",".join(paper["authors"]),
#                  "Abstract": paper["abstract"]},
#                  ignore_index=True
#                 )

# scores = [0]*len(se_conf_papers_w_abstract_df)
# for i in range(len(se_conf_papers_w_abstract_df)):
#     row_ml_score=0
#     for keyword in ml_keywords:
#         if keyword in se_conf_papers_w_abstract_df["Title"][i] or keyword in se_conf_papers_w_abstract_df["Abstract"][i]:
#             row_ml_score+=1
#     scores[i]=row_ml_score

# se_conf_papers_w_abstract_df["ml_score"] = scores

# sorted_by_ml_score = se_conf_papers_w_abstract_df.sort_values(by="ml_score", ascending=False)

# sorted_by_ml_score_100 = sorted_by_ml_score.head(100)

#######

sorted_by_ml_score_100 = pd.read_csv("C:/Users/PC/Desktop/Interaction SE with ML/SEML/top100.csv")
grouped = sorted_by_ml_score_100.groupby(by="Conf")





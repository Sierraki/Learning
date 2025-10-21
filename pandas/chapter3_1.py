import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset("tips")

# print(tips)

# fig = plt.figure(figsize=(13, 13))

# # 直方图
# axes1 = fig.add_subplot(4, 4, 1)
# axes1.hist(tips["total_bill"], bins=5)
# axes1.set_xlabel("frequency")
# axes1.set_ylabel("total bill")
# axes1.set_title("Hist")

# # 散点图
# axes2 = fig.add_subplot(4, 4, 2)
# axes2.scatter(tips["total_bill"], tips["tip"])
# axes2.set_xlabel("total_bill")
# axes2.set_ylabel("tip")
# axes2.set_title("Scatter")

# # 箱线图
# axes3 = fig.add_subplot(4, 4, 3)
# axes3.boxplot(
#     [
#         tips[tips["sex"] == "Female"]["tip"],
#         tips[tips["sex"] == "Male"]["tip"],
#     ],
#     labels=[
#         "Female",
#         "Male",
#     ],
# )
# axes3.set_xlabel("Sex")
# axes3.set_ylabel("Tip")
# axes3.set_title("Boxplot of Tips by Sex")


# plt.tight_layout()
# plt.show()


# axes4=fig.add_subplot(4,4,4)

# print(tips.columns)

# 多变量

# def recode_sex(self):
#     if self == "Female":
#         return "red"
#     return "blue"


# tips["sex_color"] = tips["sex"].apply(recode_sex)

# scatter_plot = plt.figure()
# axes1 = scatter_plot.add_subplot(1, 1, 1)
# axes1.scatter(
#     x=tips["total_bill"],
#     y=tips["tip"],
#     s=tips["size"] * 10,
#     c=tips["sex_color"],
#     alpha=0.5,
# )

# axes1.set_title("total bill vs tip colored by sex and sized by size")
# axes1.set_xlabel("total bill")
# axes1.set_ylabel("tip")

# plt.show()



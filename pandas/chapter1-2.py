import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import floor
import openpyxl
import seaborn


df = pd.read_csv(
    "Learning/pandas/pandas_for_everyone-master/data/gapminder.tsv",
    sep="\t",
)


# print(df)
# print(df.iloc[1:5, 0])
# print(df.head(5))
# # print(df.info)
# res = df.groupby(["year", "continent"])[["lifeExp", "gdpPercap"]].mean()
# # res = df.groupby(["continent"]).value_counts(["pop"])
# res.plot()
# plt.show()


# data = pd.DataFrame(
#     {"name": ["A", "B"], "age": [12, 34], "gender": ["male", "female"]},
#     index=[
#         "one",
#         "two",
#     ],
#     columns=["name", "gender", "age"],
# )

# print(df.head())
# res = df.groupby(["year"])["lifeExp"].mean()

# print(res)

# res.plot()
# plt.xlabel("year")
# plt.ylabel("pop")
# plt.show()

df = pd.read_csv("Learning/pandas/pandas_for_everyone-master/data/scientists.csv")
# print(df.columns)
# print(df)
# print(type(df["Age"].mean()))

# print(df[df["Age"] > df["Age"].mean()].loc[:, ["Name"]])


# born_date = pd.to_datetime(df["Born"], format="%Y-%m-%d")
# died_date = pd.to_datetime(df["Died"], format="%Y-%m-%d")

# df["Born"], df["Died"] = born_date, died_date

# cnt = df["Died"] - df["Born"]
# df["cnt"] = cnt

# df["cnt1"] = df["cnt"].dt.days // 365
# print(df)


# print(df)

names = df["Name"]

# print(names)

# names.to_excel("Learning\pandas\my_data.xlsx")


# res = pd.read_excel("Learning\pandas\my_data.xlsx")
# print(res)

age = df["Age"]

# print(df["Age"].mean() == df["Age"].mean(axis=0))

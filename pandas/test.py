import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_csv(
#     "Learning/pandas/pandas_for_everyone-master/data/gapminder.tsv",
#     sep="\t",
# )

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

ages = df["Age"]
print(df.head())

print(ages)
print(pd.Series([1, 100]))

print(pd.Series([1, 100]) + ages)

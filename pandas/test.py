import pandas as pd

df = pd.read_csv(
    "X:\\学习\\研究生\\代码数据库\\Learning\\pandas\\pandas_for_everyone-master\\data\\gapminder.tsv",
    sep="\t",
)


print(df.head(5))
# print(df.info)

res = df.groupby(["year", "continent"])[["lifeExp", "gdpPercap"]].mean()
print(res)

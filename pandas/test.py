import pandas as pd

df = pd.read_csv(
    "X:\\学习\\研究生\\代码数据库\\Learning\\pandas\\pandas_for_everyone-master\\data\\gapminder.tsv",
    sep="\t",
)


# print(df.head())
# print(df.info)

print(df.loc[1:30])

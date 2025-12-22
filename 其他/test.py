import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv("Learning/其他/ec_data.csv")
print(df.columns)
# 查看数据类型信息
print(df.info())
print(df.shape)
# 前五行和后五行
print(df.head(5))
print(df.tail(5))
# 数据类型分布值
print(df.describe())
# 统计每列缺失值的个数，并按缺失值个数降序排列
res = df.isnull().sum().sort_values(ascending=False)
print(res)
# 统计数量小于0的异常数个数
res = (df["Quantity"] < 0).count()
print(res)
# 删除缺失值的行，删除数量小于0的异常数据
res = df.dropna()
res = res[res["Quantity"] >= 0]
print(res)
# 使用常数100填充缺失值
res = df.fillna(100)
print(res)
# 增加一列AmountSpent=Quantity*UnitPrice，作为总价
df.loc[:, "AmountSpent"] = df["Quantity"] * df["UnitPrice"]
print(df.head())
# 查看各国家的订单数量，按降序排列
res = df["Country"].value_counts().sort_values(ascending=False)
print(res)
# 柱状图绘制各国订单数量
country_counts = df["Country"].value_counts()
country_counts.plot(kind="bar")
plt.tight_layout()
plt.show()
# 柱状图绘制各国订单金额
res = df.groupby("Country")["AmountSpent"].sum().sort_values(ascending=False)
res.plot(kind="bar")
plt.tight_layout()
plt.show()

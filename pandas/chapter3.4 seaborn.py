import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# print(tips)

# fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))  # 使用 subplots() 简化创建

# # --- 第一个子图 (ax1)：纯 KDE 曲线 ---
# # 使用 sns.kdeplot (Axes-level 函数) 并指定 ax=ax1
# ax1 = sns.kdeplot(
#     data=tips,
#     x="total_bill",
#     ax=ax1,# 绘制到第一个 Axes 上
#     color="blue",
#     fill=True,  # 填充曲线下方区域
# )
# ax1.set_title("KDE Plot")


# # --- 第二个子图 (ax2)：直方图 + KDE 曲线 ---
# # 使用 sns.histplot (Axes-level 函数) 并指定 ax=ax2
# sns.histplot(
#     data=tips,
#     x="total_bill",
#     ax=ax2,  # 绘制到第二个 Axes 上
#     kde=True,  # 同时开启 KDE 曲线
#     color="green",
#     edgecolor="black",
# )
# ax2.set_title("Histogram + KDE")


# # --- 第三个子图 (ax3)：纯直方图 ---
# # 使用 sns.histplot (Axes-level 函数) 并指定 ax=ax3
# sns.histplot(
#     data=tips,
#     x="total_bill",
#     ax=ax3,  # 绘制到第三个 Axes 上
#     # 关闭 KDE
#     color="orange",
# )
# ax3.set_title("Histogram Only")

# # 调整子图间距
# plt.tight_layout()
# plt.show()


# # 1. 创建单个 Figure 和 Axes (这是我们想要绘图的目标)
# fig, ax = plt.subplots(figsize=(8, 5))

# # 2. 使用 Axes-level 函数 sns.histplot()，并明确指定目标 Axes
# sns.histplot(
#     data=tips,
#     x="total_bill",
#     ax=ax,  # 👈 关键修正：指定将图绘制到我们创建的 ax 上
#     kde=True,
#     # 注意：在 sns.histplot 中，没有单独的 rug 参数。你需要使用 sns.rugplot
#     # color='green' 是填充色，edgecolor='black' 是边框色
#     color="green",
#     edgecolor="black",
# )

# # 3. 如果需要 Rug Plot，需要额外调用 sns.rugplot()，并指定目标 Axes
# sns.rugplot(
#     data=tips,
#     x="total_bill",
#     ax=ax,  # 👈 指定目标 Axes
#     color="darkred",
#     height=0.05,  # 控制小刻度线的高度
# )

# # 设置标题和标签
# ax.set_title("Histogram, KDE, and Rug Plot (Single Figure)")
# plt.show()


# scatter, ax = plt.subplots()

# sns.regplot(
#     data=tips,
#     x="total_bill",
#     y="tip",
#     ax=ax,
#     fit_reg=True,
# )

# plt.show()


# joint = sns.jointplot(
#     data=tips,
#     x="total_bill",
#     y="tip",
#     # 留空：jointplot 自己会处理 Figure 的创建
# )

# # 如果想在联合图的中心图上添加回归线：
# sns.regplot(
#     data=tips,
#     x="total_bill",
#     y="tip",
#     ax=joint.ax_joint,  # 关键：将回归线画在 jointplot 的中心轴上
#     scatter=False,  # 只绘制回归线，不重复绘制散点
#     color="red",
# )

# plt.show()


# hexbin = sns.jointplot(
#     x="total_bill",
#     y="tip",
#     data=tips,
#     kind="hex",
# )

# kde, ax = plt.subplots()
# ax = sns.kdeplot(
#     data=tips,
#     x="total_bill",
#     y="tip",
#    fill=False,
# )


# ked_joint = sns.jointplot(
#     data=tips,
#     x="total_bill",
#     y="tip",
#     kind="kde",
#     fill=False,
# )


# res = sns.barplot(
#     x="time",
#     y="total_bill",
#     data=tips,
#     errorbar=("ci", 100),
#     errorbar=None,
# )

# print(tips)

# box, ax = plt.subplots()
# ax = sns.violinplot(
#     data=tips,
#     x="time",
#     y="total_bill",
# )

# fig = sns.pairplot(tips)

# pair_grid = sns.PairGrid(tips)

# pair_grid = pair_grid.map_upper(sns.regplot)
# pair_grid = pair_grid.map_lower(sns.kdeplot, fill=True)
# pair_grid = pair_grid.map_diag(
#     sns.histplot,
#     kde=True,
# )
# plt.show()


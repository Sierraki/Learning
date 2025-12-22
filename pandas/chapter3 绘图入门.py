import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.gridspec as gridspec
import numpy as np

# # --- 关键设置 ---
# # 设置中文字体
# plt.rcParams["font.family"] = ["SimHei"]  # 替换为你系统上的中文字体

# # 解决负号 '-' 显示为方块的问题
# plt.rcParams["axes.unicode_minus"] = False
# # --- 关键设置结束 ---

# anscombe = sns.load_dataset("anscombe")
# # print(anscombe)
# print(anscombe.columns)

# dataset_1 = anscombe[anscombe["dataset"] == "I"]
# print(dataset_1)

# plt.plot(
#     dataset_1["x"],
#     dataset_1["y"],
#     # 线条定制
#     color="purple",  # 设置线条颜色为紫色
#     linestyle="-.",  # 设置线型为点划线
#     linewidth=2.5,  # 设置线宽
#     # 标记点定制
#     marker="D",  # 设置标记点为菱形
#     markersize=8,  # 设置标记点大小
#     markerfacecolor="red",  # 设置标记点内部颜色
#     label="AAAAA",
# )
# plt.title("2025 年 Q1 季度销售业绩对比")
# plt.xlabel("你希望显示的横轴名称")
# plt.ylabel("你希望显示的纵轴名称")
# plt.legend()
# plt.show()

# plt.plot(
#     dataset_1["x"],
#     dataset_1["y"],
#     "o",
# )
# plt.show()

# fig = plt.figure()
# axes1 = fig.add_subplot(2, 3, 1)
# axes2 = fig.add_subplot(2, 3, 2)
# axes3 = fig.add_subplot(2, 3, 3)
# axes4 = fig.add_subplot(2, 2, 4)
# plt.show()


# # 1. 创建 Figure 对象
# fig = plt.figure(figsize=(12, 6))  # 调整尺寸以更好地容纳 3 列

# # 2. 定义 2 行 x 3 列的基础网格
# gs = gridspec.GridSpec(2, 3, figure=fig)

# # --- 第一行：三个标准图 (2x3 网格中的 1, 2, 3 位置) ---

# # axes1: 位于第 0 行，第 0 列
# axes1 = fig.add_subplot(gs[0, 0])
# axes1.set_title("图 1 (1/3 宽度)")

# # axes2: 位于第 0 行，第 1 列
# axes2 = fig.add_subplot(gs[0, 1])
# axes2.set_title("图 2 (1/3 宽度)")

# # axes3: 位于第 0 行，第 2 列
# axes3 = fig.add_subplot(gs[0, 2])
# axes3.set_title("图 3 (1/3 宽度)")


# # --- 第二行：一个跨越三列的大图 ---

# # axes4: 位于第 1 行，跨越所有 3 列
# # gs[1, :] 表示“第 1 行，所有列”
# axes4 = fig.add_subplot(gs[1, :])
# axes4.set_title("图 4 (跨越整行，与 图 1-3 总宽一致)")


# # 自动调整布局，防止重叠
# fig.tight_layout()
# plt.show()


# dataset_1 = anscombe[anscombe["dataset"] == "I"]
# dataset_2 = anscombe[anscombe["dataset"] == "II"]
# dataset_3 = anscombe[anscombe["dataset"] == "III"]
# dataset_4 = anscombe[anscombe["dataset"] == "IV"]

# fig = plt.figure()

# a1 = fig.add_subplot(2, 2, 1)
# a2 = fig.add_subplot(2, 2, 2)
# a3 = fig.add_subplot(2, 2, 3)
# a4 = fig.add_subplot(2, 2, 4)

# a1.plot(dataset_1["x"], dataset_1["y"], "o", color="red")
# a2.plot(dataset_2["x"], dataset_2["y"], "o", color="red")
# a3.plot(dataset_3["x"], dataset_3["y"], "o", color="red")
# a4.plot(dataset_4["x"], dataset_4["y"], "o", color="red")

# a1.set_title("a1")
# a2.set_title("a2")
# a3.set_title("a3")
# a4.set_title("a4")

# fig.suptitle("total")

# fig.tight_layout()

# plt.show()


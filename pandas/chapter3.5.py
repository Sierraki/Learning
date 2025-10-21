import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

print(tips)


# sns.violinplot(
#     data=tips,
#     x="time",
#     y="total_bill",
#     hue="sex",
#     split=True,
#     palette={"Female": "red", "Male": "blue"},
# )

# sns.lmplot(
#     data=tips,
#     x="total_bill",
#     y="tip",
#     hue="sex",
#     fit_reg=True,
# )

# fig = sns.pairplot(tips, hue="sex")

scatter = sns.lmplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",
    fit_reg=False,
    palette={"Female": "red", "Male": "blue"},
)


plt.show()

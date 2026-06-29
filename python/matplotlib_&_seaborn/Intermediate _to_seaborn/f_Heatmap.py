import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [2, 4, 6, 8, 10],   # strongly positive with A
    "C": [5, 4, 3, 2, 1],    # strongly negative with A
    "D": [1, 5, 2, 4, 3]     # weak correlation
})

corr = df.corr()
plt.figure(figsize = (10, 8))

sns.heatmap(
    corr,
    annot = True,
    fmt = ".2f",
    cmap = "coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()


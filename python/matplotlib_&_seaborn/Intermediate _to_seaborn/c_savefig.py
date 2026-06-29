import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.savefig(
    "line_plot.png",
    dpi = 300,
    bbox_inches = "tight",
    transparent = False
)
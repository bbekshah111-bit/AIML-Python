import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 4, 5]
fig, ax = plt.subplots(2, 2, figsize = (10, 8))

ax[0, 0].plot(data)
ax[0, 0].set_title("Line")

ax[0, 1].scatter(range(len(data)), data)
ax[0, 1].set_title("Scatter")

ax[1, 0].hist(data)
ax[1, 0].set_title("Histogram")

ax[1, 1].bar(["A", "B", "C"], [10, 20, 15])
ax[1, 1].set_title("Bar")

plt.tight_layout()
plt.show()
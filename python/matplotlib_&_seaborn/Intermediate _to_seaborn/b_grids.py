import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.figure(figsize = (8, 5))
plt.plot(x, y, marker = "o")

plt.title("Quadratic Growth")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(
    linestyle = "--",
    alpha = 0.6 #visiblity of grids
)
plt.show()
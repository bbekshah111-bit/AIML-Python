import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 120]

plt.figure(figsize = (8, 5))

plt.boxplot(marks)
plt.title("Marks Distribution")
plt.ylabel("Marks")
plt.show()
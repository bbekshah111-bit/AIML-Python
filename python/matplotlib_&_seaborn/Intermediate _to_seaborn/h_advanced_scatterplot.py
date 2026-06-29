import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
plt.figure(figsize = (8, 6))

sns.scatterplot(
    data = iris,
    x = "petal_length",
    y = "petal_width",
    hue = "species",
    style = "species",
    s = 100
)

plt.title("Petal Measurement by Species")
plt.show()
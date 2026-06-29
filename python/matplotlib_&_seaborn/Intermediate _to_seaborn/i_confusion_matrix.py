from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

y = [
    "s", "s", "s", "s", "s",
    "v", "v", "v", "v", "v",
    "g", "g", "g", "g", "g"
     ]

y_pred = [
    "s", "s", "s", "s", "s",
    "v", "v", "g", "v", "v",
    "g", "v", "g", "g", "g"
]

cm = confusion_matrix(
            y,
            y_pred
        )

sns.heatmap(
            cm,
            annot=True,
            fmt = ".2f",
            xticklabels = ["Verginica", "Setosa", "Versicolor"],
            yticklabels = ["Verginica", "Setosa", "Versicolor"]
        )

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
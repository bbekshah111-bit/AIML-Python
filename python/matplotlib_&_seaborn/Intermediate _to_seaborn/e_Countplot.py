import seaborn as sns
import matplotlib.pyplot as plt

students = ["A", "A", "A", "B", "B", "C", "D"]
plt.figure(figsize = (8, 5))
sns.countplot(
    x = students,
    color = "skyblue"
)

plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Count")
plt.show()
import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]

math_marks = [78, 85, 92, 70, 88]
science_marks = [80, 82, 95, 68, 90]

all_marks = math_marks + science_marks

plt.figure(figsize = (8, 5))

#Distribution of Marks
plt.hist(
    all_marks,
    bins=5,
    color = "skyblue"
)

plt.title("Distribution of Marks")

plt.show()


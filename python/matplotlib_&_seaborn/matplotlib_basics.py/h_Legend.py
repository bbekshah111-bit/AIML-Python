import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]

math_marks = [78, 85, 92, 70, 88]
science_marks = [80, 82, 95, 68, 90]

plt.figure(figsize = (8, 5))

# Identify Multiple Lines

plt.plot(
    students,
    math_marks,
    label = "Math",
    color = "blue"
)

plt.plot(
    students,
    science_marks,
    label = "Science",
    color = "red"
)

plt.legend()

plt.title("Student Scores")

plt.show()
# A simple project to know how these works together

import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]

math_marks = [78, 85, 92, 70, 88]
science_marks = [80, 82, 95, 68, 90]

plt.figure(figsize = (10, 6))

plt.plot(
    students,
    math_marks,
    label = "Math",
    color = "blue",
    marker = "o"
)

plt.plot(
    students,
    science_marks,
    label = "Science",
    color = "red",
    marker = "s"

)

plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.legend()
plt.show()
import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]

math_marks = [78, 85, 92, 70, 88]
science_marks = [80, 82, 95, 68, 90]

plt.figure(figsize=(8, 5))

# Customize appearance
plt.plot(
    students,
    math_marks,
    color="red"
    )

plt.title("Math Scores")
plt.show()
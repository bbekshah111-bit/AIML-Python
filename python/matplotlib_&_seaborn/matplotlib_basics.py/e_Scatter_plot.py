import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]

math_marks = [78, 85, 92, 70, 88]
science_marks = [80, 82, 95, 68, 90]

plt.figure(figsize = (8, 5))

# Relationship between math and science marks
plt.scatter(
    math_marks,
    science_marks,
    color = "green"
)

plt.xlabel("Math_scores")
plt.ylabel("Science_scores")

plt.title("Math vs Science")

plt.show()
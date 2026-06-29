import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]

math_marks = [78, 85, 92, 70, 88]
science_marks = [80, 82, 95, 68, 90]

plt.figure(figsize=(8, 5))

plt.plot(students, math_marks)

# Add Title and axis names
plt.title("Math Scores")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
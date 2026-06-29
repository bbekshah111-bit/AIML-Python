import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]

math_marks = [78, 85, 92, 70, 88]
science_marks = [80, 82, 95, 68, 90]

# 1.Figure(create canvas)
plt.figure(figsize=(8, 5))

# 2.plot(line chart, show trend)
plt.plot(students, math_marks, color = "r")

# 3.Labels(add title and axis names)
plt.title("Math Scores")
plt.xlabel("Students")
plt.ylabel("marks")
plt.show()

# 4.Colors(customize appearance)

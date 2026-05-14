import matplotlib.pyplot as plt
import numpy as np

# Dataset from project 37756.jpg
students = ["AMIT", "RIYA", "JOHN"]
math_marks = [85, 92, 78]

# Bonus: Adding multiple subjects for comparative visualization
science_marks = [80, 95, 82]

# Setting up the bar positions
x = np.arange(len(students))  # Label locations
width = 0.35  # Width of the bars

fig, ax = plt.subplots(figsize=(8, 6))

# Plotting Grouped Bar Chart (Bonus Requirement)
rects1 = ax.bar(x - width/2, math_marks, width, label='Math', color='skyblue')
rects2 = ax.bar(x + width/2, science_marks, width, label='Science', color='salmon')

# Add labels, title and custom x-axis tick labels
ax.set_ylabel('Marks')
ax.set_title('Student Performance Dashboard')
ax.set_xticks(x)
ax.set_xticklabels(students)
ax.legend()

# Focus: Comparing Categories - Adding data labels on top of bars
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
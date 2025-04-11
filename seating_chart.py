import numpy as np
from numpy import random

# a. Prompt for number of rows and chairs per row
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of chairs per row: "))

# b. Predefined list of student names (make sure it's enough)
names = [
    "Abby", "Venus", "Adison", "Manali", "Dr.Kruse", "Kelly", "Grace", "Hector",
    "Ivy", "Jack", "Kara", "Leo", "Mona", "Nina", "Oscar", "Pam", "Quinn",
    "Ray", "Sara", "Tom", "Uma", "Vera", "Will", "Xena", "Yuki", "Zane"
]

names = names[:rows * cols] 

names_array = np.array(names)
random.shuffle(names_array)
seating_chart = names_array.reshape(rows, cols)

max_name_length = max(len(name) for name in names)
col_width = max_name_length + 4  # Padding for spacing

output_lines = []
output_lines.append("\nSeating Chart:\n")

for row in range(rows):
    name_line = ""
    pos_line = ""
    for col in range(cols):
        name = f"{seating_chart[row, col]:>{col_width}}"
        pos = f"({row},{col})".rjust(col_width)
        name_line += name + " "
        pos_line += pos + " "
    output_lines.append(name_line)
    output_lines.append(pos_line)

# Print to screen
print("\n".join(output_lines))

# Save to file
with open("seating_chart.txt", "w") as file:
    file.write("\n".join(output_lines))

print("\n✅ Seating chart saved to 'seating_chart.txt'")

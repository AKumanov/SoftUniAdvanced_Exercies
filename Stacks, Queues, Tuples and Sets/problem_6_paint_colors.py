# ---------------- IMPORT MODULES ------------------------
from math import floor

# ---------------- SET VARIABLES AND READ INPUT ------------------------
COLORS = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
PRIMARY_COLORS = ['red', 'yellow', 'blue']
SECONDARY_COLORS = ['orange', 'purple', 'green']
colors_data = {
    "orange": ['red', 'yellow'],
    "purple": ['red', 'blue'],
    "green": ['yellow', 'blue'],
}
collected_colors = []

line = [x for x in input().split()]

# ---------------- MAIN LOGIC ------------------------
while line:
    if len(line) >= 2:
        left_substring, right_substring = line[0], line[-1]
        temp_color = left_substring + right_substring
        reversed_color = right_substring + left_substring

        if temp_color in COLORS:
            collected_colors.append(temp_color)
            line.pop(0)
            line.pop()
            continue
        if reversed_color in COLORS:
            collected_colors.append(reversed_color)
            line.pop(0)
            line.pop()
            continue
        left_substring = line.pop(0)
        right_substring = line.pop()
        left_substring = left_substring[:-1]
        right_substring = right_substring[:-1]
        middle_index = floor(len(line) / 2)
        line.insert(middle_index, left_substring)
        line.insert(middle_index, right_substring)
    else:
        temp_color = line[0]
        if temp_color in COLORS:
            collected_colors.append(temp_color)
            line.pop()
        else:
            line.pop()

# ---------------- CHECK THE SECONDARY COLORS ------------------------
for color in collected_colors:
    if color in PRIMARY_COLORS:
        continue

    for secondary, list_of_ingredients in colors_data.items():
        if color == secondary:
            first, second = list_of_ingredients
            if first in collected_colors and second in collected_colors:
                continue
            else:
                collected_colors.remove(color)

# ---------------- PRINT THE OUTPUT ------------------------
print(collected_colors)

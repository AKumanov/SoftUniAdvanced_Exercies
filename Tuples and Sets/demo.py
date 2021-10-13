temp = {
    "orange": ['red', 'yellow'],
    "purple": ['red', 'blue'],
    "green": ['yellow', 'blue'],
}

colors = ["red", "blue", "orange"]
for color in colors:
    if color in temp.keys():
        print(type(temp[color]))
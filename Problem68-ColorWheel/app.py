prim = ["yellow", "red", "blue"]

colors = {
    "red-violet": [prim[1], "violet"],
    "violet": [prim[1], prim[2]],
    "blue-violet": [prim[2], "violet"],
    "blue-green": [prim[2], prim[0]],
    "green": [prim[2], prim[1]],
    "yellow-green": [prim[0], "green"],
    "yellow-orange": [prim[0], "orange"],
    "orange": [prim[1], prim[0]],
    "red-orange": [prim[1], "orange"],
}

count = int(input())

for line in range(count):
    colorDest = input()
    colorsNeeded = []
    for a in range(2):
        colorComponent = colors[colorDest][a]
        if colorComponent in prim:
            colorsNeeded.append(colorComponent)
        for b in range(2):
            colorsNeeded.append

    if colorDest in prim:
        print(f"No colors need to be mixed to make {colorDest}.")
    else:
        print(f"In order to make {colorDest}, {colors[colorDest][0]} and {colors[colorDest][1]} must be mixed.")
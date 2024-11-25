prim = ["yellow", "red", "blue"]

colors = {
    "violet": [prim[1], prim[2]],
    "orange": [prim[1], prim[0]],
    "blue-green": [prim[2], prim[0]]
}

count = int(input())

for i in range(count):
    colorDest = input()
    if colorDest in prim:
        print(f"No colors need to be mixed to make {colorDest}.")
    else:
        print(f"In order to make {colorDest}, {colors[colorDest][0]} and {colors[colorDest][1]} must be mixed.")
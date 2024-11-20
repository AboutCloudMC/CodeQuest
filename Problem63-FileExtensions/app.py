extensions = {}
count = int(input())

for i in range(count):
    line = input()
    ext = line.split(".")[1]
    if ext in extensions:
        extensions[ext] += 1
    else:
        extensions[ext] = 1

for ext in extensions:
    print(f"{ext} {extensions[ext]}")
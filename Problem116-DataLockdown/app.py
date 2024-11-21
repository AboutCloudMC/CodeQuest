cases = int(input())

for case in range(cases):
    lines = int(input())
    for line in range(lines):
        line = input()
        lineSplit = line.split(" ")
        url = lineSplit[0]
        size = int(lineSplit[1])
        if not url.endswith(".lmco.com") and size > 1000:
            print(" ")
            print(f"{url} {size}")

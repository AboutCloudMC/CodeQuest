import sys

extensions = {}

def read_line():
    return sys.stdin.readline().strip()
        
dataset = []
count = int(read_line())
for i in range(count):
    line = input()
    ext = line.split(".")[1]
    if ext in extensions:
        extensions[ext] += 1
    else:
        extensions[ext] = 1

for ext in extensions:
    print(f"{ext} {extensions[ext]}")


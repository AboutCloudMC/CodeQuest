import sys

def search(target, data):
    while True:
        middle = len(data)//2
        if target == data[middle]:
            return middle
        elif target > data[middle]:
            data = data[middle+1:]
        else:
            data = data[:middle-1]
        print(data)

def read_line():
    return sys.stdin.readline().strip()
        
dataset = []
count = int(read_line())
for i in range(count):
    dataset.append(int(read_line()))

print(search(6, dataset))
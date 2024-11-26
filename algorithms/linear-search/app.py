import sys

def search(item, data):
    for i in range(len(data)):
        if data[i] == item:
            return i
        
def read_line():
    return sys.stdin.readline().strip()
        
dataset = []
count = int(read_line())
for i in range(count):
    dataset.append(int(read_line()))

print(search(2, dataset))
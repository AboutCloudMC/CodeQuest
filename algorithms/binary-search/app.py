

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

dataset = [1, 3, 5, 6, 7]

print(search(6, dataset))
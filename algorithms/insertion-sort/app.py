
dataset = [5, 3, 8, 6, 1, 9, 2, 7, 4]

def sort(dataset):
    for i in range(1, len(dataset)):
        current = 0
        for j in range(i-1, 0, -1):
            if dataset[j] > i:
                current = j
        print(dataset)
        dataset[current], dataset[i] = dataset[i], dataset[current]
    dataset = sort(dataset)
    return dataset

print(sort(dataset))
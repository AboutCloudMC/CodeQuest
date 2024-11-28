
dataset = [5, 3, 8, 6, 1, 9, 2, 7, 4]

def sort(dataset):
    for i in range(len(dataset)):
        for j in range(len(dataset) - 1):
            if dataset[j] > dataset[j + 1]:
                dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
    return dataset

print(sort(dataset))
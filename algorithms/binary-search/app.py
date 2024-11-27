def bubble_sort(dataset):
    lenght = len(dataset)
    passes = lenght-1
    for i in range(passes):
        a = dataset[i]
        b = dataset[i+1]
        print(f"{a} + {b}")

data = [1, 5, 3, 5]

n = len(my_array)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        break
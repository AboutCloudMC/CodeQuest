
cases = int(input())

for _ in range(cases):
    variance = {}
    items = int(input())
    estimates = input().split()
    actual = input().split()
    difference = []
    for i in range(items):
        difference.append(float(actual[i])-float(estimates[i]))
    print(round(sum(difference)/len(difference), 2))
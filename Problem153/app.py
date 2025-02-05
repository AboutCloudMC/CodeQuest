cases = int(input())

for _ in range(cases):
    inp = input().split()
    rows = int(inp[0])
    dives = int(inp[1])
    table = []
    diveTable = []
    
    for a in range(rows):
        row = input().split()
        table.append([int(row[0]), int(row[1]), row[2], row[3]])
    
    print(table)
    for _ in range(dives):
        inp = input().split()
        depth = int(inp[0])
        time = int(inp[1])
        diveTable.append([depth, time])
        
        for b in range(len(table)):
            if table[b][0] >= depth and table[b][1] >= time:
                print(table[b][2], table[b][3])
    print(diveTable)
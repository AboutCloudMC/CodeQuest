
count = int(input())
results = []

for line in range(count):
    shift = int(input())
    line = input().upper()
    newLine = ""
    for char in line:
        if char == " ":
            newLine += char
            continue
        newASCII = ord(char)-shift
        if newASCII < 65:
            newASCII += 26
        newLine += chr(newASCII)
    results.append(newLine.lower())

for r in results:
    print(r)
    

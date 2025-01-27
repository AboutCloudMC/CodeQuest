import math

cases = int(input())
for _ in range(cases):
    launches = int(input())

    lines = []
    for _ in range(launches):
        lines.append(input())
        
    current = None
    for line in lines:
        data = line.split(" ")

        #date time cloud wind direction
        date = data[0]
        time = data[1]
        cloud = int(data[2])
        wind_speed = float(data[3])
        wind_dir = math.radians(int(data[4]))

        wind_ew = wind_speed * math.sin(wind_dir)
        wind_ns = wind_speed * math.cos(wind_dir)

        if cloud <= 1000 and abs(wind_ns) <= 20 and abs(wind_ew) <= 40:
            current = f"{date} {time}"
            break

    if current is None:
        print("ABORT LAUNCH")
    else:
        print(current)
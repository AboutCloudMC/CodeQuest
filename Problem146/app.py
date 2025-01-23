import math

cases = int(input())
for a in range(1):
    launches = int(input())
    lines = []
    for i in range(launches):
        lines.append(input()) 
    print(lines)
    for line in lines:
        print(line)
        data = line.split(" ")
        #date time cloud wind direction
        date = data[0]
        time = data[1]
        cloud = int(data[2])
        wind_speed = float(data[3])
        wind_dir = math.radians(int(data[4]))
        wind_ew = wind_speed * math.sin(wind_dir)
        wind_ns = wind_speed * math.cos(wind_dir)
        if (cloud > 1000) or (wind_ns > 20) or (wind_ew > 40):
            print("ABORT LAUNCH")
            break
        else:
            print(f"{date} {time}")
            break
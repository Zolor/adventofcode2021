data = open("input.txt").read().split("\n")

temp = True

coords = []
commands = []

for line in data:
    if line == "":
        temp = False
        continue
    if temp:
        x, y = line.split(",")
        coords.append([int(x),int(y)])
    else:
        commands.append(line)

for command in commands:
    xy, middle = command.split("=")
    xy = xy[-1]
    for coord in coords:
        if xy == "y":
            if coord[1] > int(middle):
                coord[1] = coord[1] - (coord[1] - int(middle)) * 2
        else:
            if coord[0] > int(middle):
                coord[0] = coord[0] - (coord[0] - int(middle)) * 2

maxX = 0
maxY = 0

for c in coords:
    if c[0] > maxX:
        maxX = c[0]
    elif c[1] > maxY:
        maxY = c[1]

for y in range(maxY + 1):
    line = str()
    for x in range(maxX + 1):
        if [x,y] in coords:
            line += "#"
        else:
            line += " "
    print(line)
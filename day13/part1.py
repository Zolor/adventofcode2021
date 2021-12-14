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
        if xy == y:
            if coord[1] > int(middle):
                coord[1] = coord[1] - (coord[1] - int(middle)) * 2
        else:
            if coord[0] > int(middle):
                coord[0] = coord[0] - (coord[0] - int(middle)) * 2
    break

result = []

for c in coords:
    if c not in result:
        result.append(c)

print(len(result))
data = open("input.txt").read().split("\n")

checklista2 = []
output = set()

for d in data:
    från, till = d.split(" -> ")
    x1, y1 = från.split(",")
    x2, y2 = till.split(",")
    x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
    if x1 == x2:
        if y1 > y2:
            checklista2.append(set(str(x2) + "," + str(i) for i in range(y2, y1 + 1)))
        elif y2 > y1:
            checklista2.append(set(str(x1) + "," + str(i) for i in range(y1, y2 + 1)))
    elif y1 == y2:
        if x1 > x2:
            checklista2.append(set(str(i) + "," + str(y2) for i in range(x2, x1 + 1)))
        elif x2 > x1:
            checklista2.append(set(str(i) + "," + str(y1) for i in range(x1, x2 + 1)))
    else:
        if x1 > x2:
            if y1 > y2:
                checklista2.append(set(str(x2 + i) + "," + str(y2 + i) for i in range(x1-x2 + 1)))
            elif y2 > y1:
                checklista2.append(set(str(x1 - i) + "," + str(y1 + i) for i in range(x1-x2 + 1)))
        elif x2 > x1:
            if y1 > y2:
                checklista2.append(set(str(x2 - i) + "," + str(y2 + i) for i in range(x2-x1 + 1)))
            elif y2 > y1:
                checklista2.append(set(str(x1 + i) + "," + str(y1 + i) for i in range(x2-x1 + 1)))

for line in checklista2:
    for line2 in checklista2:
        if line == line2:
            continue
        output|=line&line2

print(len(output))
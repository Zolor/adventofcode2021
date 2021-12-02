data = open("testinput.txt").read().split("\n")

depth = 0
hor = 0

for line in data:
    d, h = line.split()
    if d == "forward":
        hor += int(h)
    elif d == "up":
        depth -= int(h)
    elif d == "down":
        depth += int(h)

print(depth * hor)
data = open("input.txt").read().split("\n")

depth = 0
hor = 0
aim = 0

for line in data:
    d, h = line.split()
    if d == "forward":
        hor += int(h)
        depth += aim * int(h)
    elif d == "up":
        aim -= int(h)
    elif d == "down":
        aim += int(h)
print(depth * hor)
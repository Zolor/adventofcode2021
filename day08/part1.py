data = open("input.txt").read().split("\n")
counter = 0

for line in data:
    signal, digit = line.split("|")

    for d in digit.split():
        if len(d) in [2, 3, 4, 7]:
            counter += 1

print(counter)
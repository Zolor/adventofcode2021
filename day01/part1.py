data = open("input.txt").read().split("\n")
count = 0
prev = 0

for i in data:
    if prev == 0:
        prev = int(i)
        continue
    elif int(i) > prev:
        count += 1
        prev = int(i)
    prev = int(i)

print(count)
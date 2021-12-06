data = open("input.txt").read().split(",")

data = list(map(int, data))

days = 0

fish = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

for i in data:
    fish[i] += 1

tmpdict = fish.copy()

while days != 256:
    print(fish)
    tmp8 = fish[8]
    for k, v in fish.items():
        if k == 0:
            tmp6 = fish[6]
            tmpdict[6] = v
            tmpdict[8] = v
        elif k == 6:
            tmpdict[5] = tmp6
        elif k == 7:
            tmpdict[6] += v
            tmpdict[k] = tmp8
        else:
            tmpdict[k-1] = v
            
    days += 1
    fish = tmpdict.copy()

print(sum(fish.values()))


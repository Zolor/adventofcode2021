fish = open("input.txt").read().split(",")

fish = list(map(int, fish))

days = 0
tmplist = fish.copy()

while days != 80:
    #print(fish)
    for x, f in enumerate(fish):
        if f == 0:
            tmplist[x] = 6
            tmplist.append(8)
        else:
            tmplist[x] = f - 1
    days += 1
    fish = tmplist.copy()

print(len(fish))
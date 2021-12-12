data = open("input.txt").read().split("\n")

comp = data[0]
counter = 0
map = {}

for y, l in enumerate(data):
    for x, r in enumerate(l):
        map[x,y] = int(r)

while True:
    for k, v in map.items():
        map[k] = v + 1
    flashing = True
    tmp_list = []
    while flashing == True:
        flashing = False
        for k, v in map.items():
            if v > 9:
                map[k] = 0
                tmp_list.append(k)
                flashing = True
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if k[0] + x >= 0 and k[1] + y >= 0 and k[0] + x < len(comp) and k[1] + y < len(data):
                            check = map.get((k[0] + x,k[1] + y))
                            if check == 0 and (k[0] + x,k[1] + y) in tmp_list:
                                continue
                            else:
                                map[(k[0] + x,k[1] + y)] = check + 1
    counter += 1
    if len(tmp_list) == len(map):
        print(counter)
        break

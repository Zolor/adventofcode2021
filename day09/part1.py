data = open("input.txt").read().split("\n")

comp = data[0]

ans = 0

map = {}

for y, l in enumerate(data):
    for x, r in enumerate(l):
        map[x,y] = int(r)

for k, v in map.items():
    v = int(v)
    check = True
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if k[0] + x >= 0 and k[1] + y >= 0 and k[0] + x < len(comp) and k[1] + y < len(data):
                    if v >= map.get((k[0] + x,k[1] + y)) and ((x == 0 and y in [1,-1]) or (x in [1,-1] and y == 0)):
                        check = False
                
    if check == True:
        ans += int(v) + 1

print(ans)

import copy

data = open('input.txt').readlines()
karta = [[int(j) for j in i.strip()]for i in data]

#Extending the list vertically
for line in karta:
    tmp_line = copy.deepcopy(line)
    for x in range(1,5):
        for n in tmp_line:
            if n + x > 9:
                line.append(n + x - 9)
            else:
                line.append(n + x)
#Extending horizontally
tmp_karta = copy.deepcopy(karta)
for x in range(1,5):
    for line in karta:
        tmp_line = []
        for n in line:
            if n + x > 9:
                tmp_line.append(n + x - 9)
            else:
                tmp_line.append(n + x)
        tmp_karta.append(tmp_line)

karta = tmp_karta

visited = [[False for _ in i.strip()]for i in data]
karta[0][0] = 0
for x in range(len(karta)):
    for y in range(len(karta[0])):
        if x == 0 and y == 0:
            continue
        elif x == 0:
            karta[x][y] += karta[x][y-1]
        elif y == 0:
            karta[x][y] += karta[x-1][y]
        else:
            karta[x][y] += min(karta[x-1][y],karta[x][y-1])
#for m in karta:
#    print(m)
print(karta[len(karta)-1][len(karta[0])-1])

#2789 too high
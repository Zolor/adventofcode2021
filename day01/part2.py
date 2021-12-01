data = open("testinput.txt").read().split("\n")
count = 0
prev = False
lista = []
lista2 = []

for x, i in enumerate(data):
    if prev == False:
        lista.append(int(i))
        lista2.append(int(data[x+1]))
        prev = True
        continue
    elif len(lista) != 3 and x+1 < len(data):
        lista.append(int(i))
        lista2.append(int(data[x+1]))
    if len(lista) == 3:
        if sum(lista) < sum(lista2):
            count +=1

        lista.pop(0)
        lista2.pop(0)
        

print(count)
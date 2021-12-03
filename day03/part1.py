data = open("input.txt").read().split("\n")

gamma = 0
epsilon = 0
lista0 = []
lista1 = []

for a in data[0]:
    lista0.append(0)
    lista1.append(0)
    
for line in data:
    for x, n in enumerate(line):
        if n == "0":
            lista0[x] = lista0[x] + 1
        elif n == "1":
            lista1[x] = lista1[x] + 1

gamma = "0b"
epsilon = "0b"
for z, o in zip(lista0, lista1):
    if z > o:
        gamma+="0"
        epsilon+="1"
    else:
        gamma+="1"
        epsilon+="0"
print(int(gamma, 2)*int(epsilon, 2))
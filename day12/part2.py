data = open("input.txt").read().split("\n")

karta = {}

for line in data:
    o, t = line.split("-")
    if o in karta.keys():
        karta.get(o).append(t)
    else:
        karta[o] = [t]
    if t in karta.keys():
        karta.get(t).append(o)
    else:
        karta[t] = [o]

def rekursiva(lista, kartan):
    if lista[-1] == "end":
        return(lista)
    tmplista = []
    for x in kartan.get(lista[-1]):
        temp = lista + [x]
        if x.islower() and len([y for y in temp if temp.count(y) > 1 and y.islower()]) > 2:
            continue
        elif x != "start":
            tmplista.extend(rekursiva(lista + [x], karta))
    return(tmplista)

lol = rekursiva(["start"], karta)

print(lol.count("start"))
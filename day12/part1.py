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
        if x.islower() and x in lista:
            continue
        elif x != "start":
            tmplista.extend(rekursiva(lista + [x], karta))
    if len(tmplista) == 1:
        return(tmplista[0])
    return(tmplista)

lol = rekursiva(["start"], karta)

print(lol.count("start"))
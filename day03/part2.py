data = open("input.txt").read().split("\n")

def co2(lista, ett, noll):
    counter = 0
    while len(lista) > 1:
        tmp0 = 0
        tmp1 = 0
        tmplist = []
        for line in lista:
            if line[counter] == "0":
                tmp0+=1
            elif line[counter] == "1":
                tmp1+=1
        if tmp0 > tmp1:
            tmplist = [x for x in lista if x[counter] == ett]
        elif tmp0 < tmp1:
            tmplist = [x for x in lista if x[counter] == noll]
        elif tmp0 == tmp1:
            tmplist = [x for x in lista if x[counter] == noll]
        counter+=1
        lista = tmplist
    
    return(int(lista[0], 2))

first = co2(data, "1", "0")
second = co2(data, "0", "1")

print(first*second)
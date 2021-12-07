import statistics

data = list(map(int, open("input.txt").read().split(",")))

def calcis(t):
    result = 0
    for n in data:
        if n == t:
            continue
        elif n < t:
            for x in range(1, t - n + 1):
                result += x
        else:
            for x in range(1, n - t + 1):
                result += x
    return(result)

lista = []

for d in range(max(data)):
    lista.append(calcis(d))

print(min(lista))

#98363819 too high
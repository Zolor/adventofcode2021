data = open("testinput.txt").read().split("\n")

dct = {line.split(" -> ")[0]:line.split(" -> ")[1] for line in data if "->" in line}
word = data[0]
checklist = list(set(line.split("-> ")[1] for line in data if "->" in line))

for _ in range(40):
    tmpword = str()
    for x, i in enumerate(word):
        if x + 1 >= len(word):
            tmpword += i
            break
        elif i + word[x+1] in dct.keys():
            tmpword += i + dct.get(i + word[x+1])
    word = tmpword

maxA = 0
minA = 0
for c in checklist:
    if maxA < word.count(c):
        maxA = word.count(c)
    if minA == 0 or minA > word.count(c):
        minA = word.count(c)

print(maxA - minA)
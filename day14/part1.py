data = open("testinput.txt").read().split("\n")

dct = {line.split(" -> ")[0]:line.split(" -> ")[1] for line in data if "->" in line}
word = data[0]

print(word, dct)
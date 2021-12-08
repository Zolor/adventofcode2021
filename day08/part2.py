data = open("testinput.txt").read().split("\n")
counter = 0

for line in data:
    signal, digit = line.split("|")
    digits = {0:"", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:""}
    signal = [s for s in signal.split()]
    mapper = [0, 0, 0, 0, 0, 0, 0]
    for s in signal:
        if len(s) == 2:
            digits[1] = s
        elif len(s) == 3:
            digits[7] = s
        elif len(s) == 4:
            digits[4] = s
        elif len(s) == 7:
            digits[8] = s
    mapper[0] = [n for n in digits[7] if n not in digits[1]]
    print(digits)
    print(signal)

print(counter)
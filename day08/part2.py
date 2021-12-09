data = open("input.txt").read().split("\n")
counter = 0
result = 0
for line in data:
    signal, digit = line.split("|")
    digits = {0:"", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:""}
    signal = [s for s in signal.split()]
    mapper = [0, 0, 0, 0, 0, 0, 0]
    fiver = []
    sixer = []
    for s in signal:
        if len(s) == 2:
            digits[1] = s
        elif len(s) == 3:
            digits[7] = s
        elif len(s) == 4:
            digits[4] = s
        elif len(s) == 5:
            fiver.append(s)
        elif len(s) == 6:
            sixer.append(s)
        elif len(s) == 7:
            digits[8] = s
    mapper[0] = [n for n in digits[7] if n not in digits[1]][0]

    #find 9
    combo = set(digits[4] + digits[7])
    for s in sixer:
        test = [n for n in s if n not in combo]
        if len(test) == 1:
            mapper[6] = test[0]
            digits[9] = s
            sixer.remove(s)
            break
    #find 2
    for s in fiver:
        test = [n for n in s if n not in digits[9]]
        if len(test) == 1:
            mapper[4] = test[0]
            digits[2] = s
            fiver.remove(s)
            break
    #find 3 and 5
    for s in fiver:
        test = [n for n in s if n not in digits[7]]
        if len(test) == 2:
            digits[3] = s
            fiver.remove(s)
            break
    digits[5] = fiver[0]
    #find 0 and 6
    digits[6] = digits[5] + mapper[4]
    for s in sixer:
        if sorted(s) == sorted(digits[6]):
            sixer.remove(s)
            break
    digits[0] = sixer[0]
    #Time to calc!
    code = digit.strip().split(" ")
    decode = str()
    for c in code:
        decode += str([k for k, v in digits.items() if sorted(v) == sorted(c)][0])
            
    result += int(decode)

print(result)
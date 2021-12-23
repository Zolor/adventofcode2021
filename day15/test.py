import copy
karta = [[1,2,3]]

for line in karta:
    print(line)
    tmp_line = copy.deepcopy(line)
    for x in range(1):
        for n in tmp_line:
            if n + x > 9:
                line.append(1)
            else:
                line.append(n + x)
    line = tmp_line
    print(karta)

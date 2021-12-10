data = open("input.txt").read().split("\n")

incomplete = []
score = []
for line in data:
    openers = []
    bonk = False
    for l in line:
        if l in ["(", "[", "{", "<"]:
            openers.append(l)
        elif l in [")", "]", "}", ">"]:
            if (l == ")" and openers[-1] == "(") or (l == "]" and openers[-1] == "[") or (l == "}" and openers[-1] == "{") or (l == ">" and openers[-1] == "<"):
                openers = openers[:-1]
            else:
                bonk = True
                break
    if bonk == False:
        incomplete.append(line)

for line in incomplete:
    openers = []
    tmpscore = 0
    for l in line:
        if l in ["(", "[", "{", "<"]:
            openers.append(l)
        elif l in [")", "]", "}", ">"]:
            if (l == ")" and openers[-1] == "(") or (l == "]" and openers[-1] == "[") or (l == "}" and openers[-1] == "{") or (l == ">" and openers[-1] == "<"):
                openers = openers[:-1]
    for l in reversed(openers):
        if l == "(":
            tmpscore *= 5
            tmpscore += 1
        elif l == "[":
            tmpscore *= 5
            tmpscore += 2
        elif l == "{":
            tmpscore *= 5
            tmpscore += 3
        elif l == "<":
            tmpscore *= 5
            tmpscore += 4
    score.append(tmpscore)

score = sorted(score)
print(score[int((len(score) - 1)/2)])

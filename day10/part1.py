data = open("input.txt").read().split("\n")

bonkers = []

for line in data:
    openers = []
    for l in line:
        if l in ["(", "[", "{", "<"]:
            openers.append(l)
        elif l in [")", "]", "}", ">"]:
            if (l == ")" and openers[-1] == "(") or (l == "]" and openers[-1] == "[") or (l == "}" and openers[-1] == "{") or (l == ">" and openers[-1] == "<"):
                openers = openers[:-1]
            else:
                bonkers.append(l)
                break

result = 0
for s in bonkers:
    if s == ")":
        result += 3
    elif s == "]":
        result += 57
    elif s == "}":
        result += 1197
    elif s == ">":
        result += 25137

print(result)
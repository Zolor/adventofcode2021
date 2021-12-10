data = open("input.txt").read().split("\n")

bonkers = []
result = 0
for line in data:
    openers = []
    for l in line:
        if l in ["(", "[", "{", "<"]:
            openers.append(l)
        elif l in [")", "]", "}", ">"]:
            if (l == ")" and openers[-1] == "(") or (l == "]" and openers[-1] == "[") or (l == "}" and openers[-1] == "{") or (l == ">" and openers[-1] == "<"):
                openers = openers[:-1]
            else:
                if l == ")":
                    result += 3
                elif l == "]":
                    result += 57
                elif l == "}":
                    result += 1197
                elif l == ">":
                    result += 25137
                break

print(result)
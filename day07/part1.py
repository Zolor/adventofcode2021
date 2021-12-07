import statistics

data = open("input.txt").read().split(",")


data = list(map(int, data))

median = statistics.median(data)

result = 0

for n in data:
    if n < median:
        result += median - n
    else:
        result += n - median

print(result)
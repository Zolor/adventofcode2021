data = open("input.txt").read().split("\n")

x, y = data[0].strip("target area: ").split(",")
x = x.strip("x=")
y = y.strip(" y=")

target_area = [[m,n] for m in range(int(x.split("..")[0]),int(x.split("..")[1])+1) for n in range(int(y.split("..")[0]),int(y.split("..")[1])+1)]
min_x, max_x = [int(b) for b in x.split("..")]
min_y, max_y = [int(b) for b in y.split("..")]
test_probe = [0,0]
hits = []

for x in range(1, max_x + 1):
    for y in range(min_y, 2000):
        test_probe[0] = x
        test_probe[1] = y
        tmp_x = x
        tmp_y = y
        for _ in range(2000):
            if test_probe[0] >= min_x and test_probe[0] <= max_x and test_probe[1] >= min_y and test_probe[1] <= max_y:
                hits.append([x, y])
                break
            elif test_probe[0] > max_x:
                break
            tmp_y -= 1
            test_probe[1] += tmp_y
            if tmp_x > 0:
                tmp_x -= 1
                test_probe[0] += tmp_x

print(len(hits))

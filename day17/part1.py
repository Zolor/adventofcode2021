data = open("input.txt").read().split("\n")

x, y = data[0].strip("target area: ").split(",")
x = x.strip("x=")
y = y.strip(" y=")

target_area = [[m,n] for m in range(int(x.split("..")[0]),int(x.split("..")[1])+1) for n in range(int(y.split("..")[0]),int(y.split("..")[1])+1)]
min_x, max_x = [int(b) for b in x.split("..")]
min_y, max_y = [int(b) for b in y.split("..")]
max_peak = 0
test_probe = [0,0]

for x in range(1, max_x + 1):
    for y in range(1, 1000):
        test_probe[0] = x
        test_probe[1] = y
        peak = y
        tmp_x = x
        tmp_y = y
        for _ in range(1000):
            tmp_y -= 1
            test_probe[1] += tmp_y
            if tmp_x > 0:
                tmp_x -= 1
                test_probe[0] += tmp_x
            if peak < test_probe[1]:
                peak = test_probe[1]
            if test_probe[0] >= min_x and test_probe[0] <= max_x and test_probe[1] >= min_y and test_probe[1] <= max_y:
                if max_peak < peak:
                    max_peak = peak
                break
            elif test_probe[0] > max_x or test_probe[1] < min_y:
                break

print(max_peak)

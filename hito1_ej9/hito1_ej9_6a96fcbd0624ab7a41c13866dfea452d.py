x1, y1, n1, x2, y2, n2 = (
    int(input()),
    int(input()),
    int(input()),
    int(input()),
    int(input()),
    int(input()),
)


matriz = [int(x1), int(y1), int(n1), int(x2), int(y2), int(n2)]

matriz[0] *= x2
matriz[1] *= x2
matriz[2] *= x2
matriz[3] *= x1
matriz[4] *= x1
matriz[5] *= x1

y = (matriz[2] - matriz[5]) / (matriz[1] - matriz[4])
x = (n1 - y * y1) / x1

print("x=" + str(x))
print("y=" + str(y))

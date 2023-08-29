num = input("Ingrese un numero de hasta 4 digitos: ")
digi = [int(a) for a in str(num)]

if len(digi) >= 4:
    m = digi[0]
    c = digi[1]
    d = digi[2]
    u = digi[3]
    print(str(m) + "M + " + str(c) + 'C + ' + str(d) + "D + " + str(u) + "U ")
elif len(digi) >= 3:
    c = digi[0]
    d = digi[1]
    u = digi[2]
    print(str(c) + 'C + ' + str(d) + "D + " + str(u) + "U ")
elif len(digi) >= 2:
    d = digi[0]
    u = digi[1]
    print(str(d) + "D + " + str(u) + "U ")
elif len(digi) >= 1:
    u = digi[0]
    print(str(u) + "U ")

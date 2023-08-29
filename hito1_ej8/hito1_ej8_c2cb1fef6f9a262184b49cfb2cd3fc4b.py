x= input("Ingrese un numero para descomponerlo: ")


if len(x) == 4:
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    print(x1+"M + " + x2 + "C + " + x3 + "D + "+ x4 + "U")
elif len(x) == 3:
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    print(x1 + "C + " + x2 + "D + "+ x3 + "U")
elif len(x) == 2:
    x1 = x[0]
    x2 = x[1]
    print(x1 + "D + "+ x2 + "U")
elif len(x) == 1:
    x1 = x[0]
    print(x1 + "U")
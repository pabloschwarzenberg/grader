#Descomponer un número
num = str(input("Ingrese un número de hasta 4 dígitos: "))
cont = 1
for i in num:
    if len(num) == 1:
        U = i + "U"
        print(U)
    if len(num) == 2:
        if cont == 1:
            D = i + "D"
        elif cont == 2:
            U = i + "U"
            print(D + " + " + U)
    elif len(num) == 3:
        if cont == 1:
            C = i + "C"
        elif cont == 2:
            D = i + "D"
        elif cont == 3:
            U = i + "U"
            print(C + " + " + D + " + " + U)
    elif len(num) == 4:
        if cont == 1:
            M = i + "M"
        elif cont == 2:
            C = i + "C"
        elif cont == 3:
            D = i + "D"
        elif cont == 4:
            U = i + "U"
            print(M + " + " + C  + " + " + D + " + " + U)
    cont += 1     
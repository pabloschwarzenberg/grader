n = int(input("ingrese un numero de hasta 4 digitos >"))
if n <= 9999 and n >= 999:
    n = str(n)
    n = list(n)

    M = n[-4]
    C = n[-3]
    D = n[-2]
    U = n[-1]

    print(M,"M + ",C,"C + ",D,"D + ",U,"U")

elif n <= 999 and n >= 99:
    n = str(n)
    n = list(n)

    C = n[-3]
    D = n[-2]
    U = n[-1]

    print(C,"C + ",D,"D + ",U,"U")

elif n <= 99 and n >= 9:
    n = str(n)
    n = list(n)

    D = n[-2]
    U = n[-1]

    print(D,"D + ",U,"U")

elif n <= 9 and n >= 0:
    n = str(n)
    n = list(n)

    U = n[-1]

    print(U,"U")
else:
    print("Numero Incorrecto intentelo otra vez")
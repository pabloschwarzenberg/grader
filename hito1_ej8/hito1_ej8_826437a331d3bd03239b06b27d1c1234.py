#Descomponer un número
x = int(input("Dame un numero entero de 1,2,3 o 4 ciras: "))
if x > 9999:
    print("Debe ser un numero de 4 cifras maximo")
elif x > 999:
    x = str(x)
    M = x[0:1]
    C = x[1:2]
    D = x[2:3]
    U = x[3:4]
    print(M, "M+", C, "C+", D, "D+", U, "U")
elif x > 99:
    x = str(x)
    C = x[0:1]
    D = x[1:2]
    U = x[2:3]
    print(C, "C+", D, "D+", U, "U")
elif x > 9:
    x = str(x)
    D = x[0:1]
    U = x[1:2]
    print(D, "D+", U, "U")
else:
    x = str(x)
    U = x[0:1]
    print(U, "U")
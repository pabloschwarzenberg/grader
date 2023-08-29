#Descomponer un número
NUMERO= int(input("escribe un numero de hasta 4 digitos:"))

#DESCOMPOSICION

AX= str(NUMERO)
B= AX[0]


if (NUMERO > 0) and (NUMERO < 10):
    print(B+"U")
else:
    if (NUMERO > 9) and (NUMERO < 100):
        C= AX[1]
        print(B+"D""+"+C+"U")
    else:
        if (NUMERO > 99) and (NUMERO < 1000):
            C= AX[1]
            D= AX[2]
            print(B+"C""+"+C+"D""+"+D+"U")
        else:
            if (NUMERO > 999) and (NUMERO < 10000):
                C= AX[1]
                D= AX[2]
                E= AX[3]
                print(B+"M""+"+C+"C""+"+D+"D""+"+E+"U")      
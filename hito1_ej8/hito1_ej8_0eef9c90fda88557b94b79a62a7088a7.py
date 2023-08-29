#Descomponer un número
numero = int(input("Dame un numero de 4 digitos: ")) #1230

M = numero // 1000
C = (numero // 100) % 10
D = (numero // 10) % 10
U = numero % 10
if len(str(numero)) == 1:
    print(str(U)+"U")
elif len(str(numero)) == 2:
    print(str(D)+"D"+"+"+str(U)+"U")
elif len(str(numero)) == 3:
    print(str(C)+"C"+"+"+str(D)+"D"+"+"+str(U)+"U")
elif len(str(numero)) == 4:
    print(str(M)+"M"+"+"+str(C)+"C"+"+"+str(D)+"D"+"+"+str(U)+"U")
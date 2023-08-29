#Descomponer un número
numero = int(input("ingresa el numero: "))
M = str(numero //1000)
numero = numero % 1000
C = str(numero //100)
numero = numero % 100
D = str(numero //10)
numero = numero % 10
U = str(numero //1)
#print(M, C, D, U)
if int(M) >= 1 and int(M)<=9:
    print(M +"M +", C+"C +", D+"D +", U+"U")
elif int(C) >= 1 and int(C)<=9:
    print(C+"C +", D+"D +", U+"U")
elif int(D) >= 1 and int(D)<=9:
    print(D+"D +", U+"U")
else:
    if int(U) >= 1 and int(U)<=9:
        print(U+"U")      
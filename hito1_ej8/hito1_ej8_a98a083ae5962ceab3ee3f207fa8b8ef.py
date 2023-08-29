#Descomponer un número
numero=int(input("Ingrese un numero de hasta 4 digitos"))

ind = 1
conta=numero
while (conta) >= 10:
    conta = conta / 10
    ind = ind + 1
    
#print("Digitos:", ind)
#print(numero)


if ind==4:
    n=str(numero)
    M=n[0]
    C=n[1]
    D=n[2]
    U=n[3]
    print(M+ "M +", C+ "C +", D+ "D +", U+ "U")

elif ind==3:
    n = str(numero)
    C = n[0]
    D = n[1]
    U = n[2]
    print(C + "C +", D + "D +", U + "U")

elif ind==2:
    n = str(numero)
    D = n[0]
    U = n[1]
    print(D + "D +", U + "U")

elif ind==1:
    n = str(numero)
    U = n[0]
    print(U + "U")
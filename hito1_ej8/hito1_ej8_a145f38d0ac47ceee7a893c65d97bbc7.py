#Descomponer un número
numero=(str(input("ingrese numero de hasta 4 digitos ",)))
if(len(numero)==4):
    M = int(numero[0])
    C = int(numero[1:2])
    D = int(numero[2:3])
    U = int(numero[3:4])
    print("{}M+{}C+{}D+{}U".format(M, C, D, U))
elif(len(numero)==3):
    C = int(numero[0])
    D = int(numero[1:2])
    U = int(numero[2:3])
    print("{}C+{}D+{}U".format(C, D, U))
elif(len(numero)==2):
    D = int(numero[0])
    U = int(numero[1:2])
    print("{}D+{}U".format(D, U))
elif(len(numero)==1):
    U = int(numero[0])
    print("{}U".format(U))
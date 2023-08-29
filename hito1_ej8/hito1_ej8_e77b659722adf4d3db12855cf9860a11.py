#Descomponer un número
numero = int(input("ingrese valor:"))

M = numero / 1000
tmp = numero % 1000

C = tmp / 100
tmp = tmp % 100

D = tmp / 10
U = tmp % 10


print("%i"%M+"M+", "%i"%C+"C+", "%i"%D+"D+", "%i"%U+"U")
if(M==0):
    print("%i"%C+"C+", "%i"%D+"D+", "%i"%U+"U")
else:
    if((M==0) and (C==0)):
        print( "%i"%D+"D+", "%i"%U+"U")
    else:
        if((M==0) and (C==0) and (D==0)):
            print("%i"%U+"U")
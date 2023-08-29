#Factores Primos
Numero=int(input("ingrese un numero entero:"))
factor=2
while Numero > 1:
    if Numero % factor == 0:
        print(factor)
        Numero//=factor
    else:
        factor+=1
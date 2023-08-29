#Factores Primos
#un numero primo solo es divisible por 1 y por si mismo
numero = int(input("ingrese numero: "))
x = 2
while (numero != 1):
    if(numero %x == 0):
        print(x)
        numero = numero/x;
    else:
        x = x + 1
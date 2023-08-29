#Factores Primos
x = int(2)
numero = int(input("Favor ingrese el numero para calcular el factor primo: "))

while (numero != 1):
    if (numero % x == 0):
        print(str(x)+" ");
        numero=numero/x;

    else:
        x = x +1;
#Factores Primos
numero = int(input("Ingrese un número entero: "))
x = int(2)

while (numero != 1):
    if numero%x == 0:
        print(str(x) + "")
        numero = numero / x
    else:
        x = x + 1
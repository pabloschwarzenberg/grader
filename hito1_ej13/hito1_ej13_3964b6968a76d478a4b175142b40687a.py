#Factores Primos
x = int(2)
numero_primos = int(input("Ingrese el numero: "))
while(numero_primos != 1):
    if (numero_primos % x == 0 ):
        print(str(x) + "")
        numero_primos = numero_primos / x
    else:
        x = x + 1
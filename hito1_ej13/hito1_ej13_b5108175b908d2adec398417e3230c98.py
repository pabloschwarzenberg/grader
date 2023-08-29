#Factores Primos
numero = int(input("Ingrese un numero entero: "))
for i in range(2, numero+1):
    while numero % i == 0:
        print(i)
        numero = numero / i

     
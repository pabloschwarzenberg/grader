#Factores Primos
numero = int(input("Ingrese un numero entero: "))
n = 2
A = []
while n <= numero:
    if (numero % n) == 0:
        print(n)
        numero = numero/n
    else:
        n += 1

print(A)

#Factores Primos
numerito = int(input("Ingrese un número entero: "))
p = int(2)

while (numerito != 1):
    if numerito%p == 0:
        print(str(p) + "")
        numerito = numerito / p
    else:
        p = p + 1

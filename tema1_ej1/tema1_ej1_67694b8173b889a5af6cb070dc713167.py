#Suma de los N primeros número
n = int(input("ingresa un numero mayor o igual a 1:"))
x = n*(n + 1)//2

if n <= 1:
    print("Numero ingresado no valido, intente nuevamente")
elif n > 1:
    print(x)
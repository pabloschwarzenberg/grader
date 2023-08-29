#Factores Primos
x = int(input("Ingrese un número entero: "))
for i in range(1,x):
    if x % i == 0:
        print(i)
        
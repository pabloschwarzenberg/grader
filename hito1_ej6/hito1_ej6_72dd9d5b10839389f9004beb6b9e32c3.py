#Ordenar tres números
num1 = int(input("Ingrese el primer número:"))
num2 = int(input("Ingrese el segundo número:"))
num3 = int(input("Ingrese el tercer número:"))

menor = num1
medio = num2
mayor = num3

if num2 < menor:
    menor = num2
    medio = num1

if num3 < menor:
    menor = num3
    medio = num1
    mayor = num2
elif num3 < medio:
    medio = num3
    mayor = num2

print("Los números ordenados de menor a mayor son:", menor, ",", medio, ",", mayor)
# Pedir al usuario que ingrese tres números enteros
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

#Lista con los tres números
numeros = [num1, num2, num3]

# Ordenar la lista de menor a mayor
numeros.sort()

print(*numeros, sep=",")

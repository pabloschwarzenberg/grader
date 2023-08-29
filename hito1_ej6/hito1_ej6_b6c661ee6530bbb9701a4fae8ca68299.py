#Ordenar tres números
num1 = int(input("Escribe un numero entero: "))
num2 = int(input("Escribe un numero entero: "))
num3 = int(input("Escribe un numero entero: "))

numeros = [num1, num2, num3]
ordenados = sorted(numeros)

print(ordenados[0],",",ordenados[1],",",ordenados[2])
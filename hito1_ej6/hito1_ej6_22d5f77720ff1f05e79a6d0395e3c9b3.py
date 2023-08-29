#Ordenar tres números
a = int(input("Ingrese numero entero: "))
b = int(input("Ingrese numero entero: "))
c = int(input("Ingrese numero entero: "))

numeros = a, b, c

numeros_ordenados = sorted(numeros)

print("El orden de numeros de menor a mayor es: ",numeros_ordenados)      
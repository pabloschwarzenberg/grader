#Ordenar tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

numeros = [num1, num2, num3]

numeros.sort()

print("Los números ordenados son:", ", ".join(map(str, numeros)))

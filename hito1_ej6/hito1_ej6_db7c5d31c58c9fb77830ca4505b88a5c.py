#Ordenar tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

numeros_ordenados = sorted([num1, num2, num3])

print("Los números ordenados de menor a mayor son:", ", ".join([str(num) for num in numeros_ordenados]))
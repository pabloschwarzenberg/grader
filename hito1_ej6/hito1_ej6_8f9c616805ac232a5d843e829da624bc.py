#Ordenar tres números
# Solicitar al usuario los tres números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

# Ordenar los números de menor a mayor
min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)
mid_num = (num1 + num2 + num3) - min_num - max_num

# Imprimir los números ordenados separados por comas
print(min_num, mid_num, max_num, sep=", ")

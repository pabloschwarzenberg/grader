#Ordenar tres números
# Pedir al usuario que ingrese los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Encontrar el número más pequeño
min_num = min(num1, num2, num3)

# Encontrar el número más grande
max_num = max(num1, num2, num3)

# Calcular el número del medio
med_num = num1 + num2 + num3 - min_num - max_num

# Imprimir los números ordenados
print("Números ordenados: " + str(min_num) + ", " + str(med_num) + ", " + str(max_num))

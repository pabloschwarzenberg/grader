 #Entrada
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Encontrar el número menor
if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

# Encontrar el número mayor
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# Encontrar el número medio
if menor == num1:
    if mayor == num2:
        medio = num3
    else:
        medio = num2
elif menor == num2:
    if mayor == num1:
        medio = num3
    else:
        medio = num1
else:
    if mayor == num1:
        medio = num2
    else:
        medio = num1

# Imprimir los números ordenados separados por comas
print("Los números ordenados de menor a mayor son:", menor, ",", medio, ",", mayor)
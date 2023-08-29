#Ordenar tres números
num1 = int(input("Ingresa el primer número "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Ordenar los números de menor a mayor
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1

# Imprimir los números ordenados
print(num1, ",", num2, ",", num3)
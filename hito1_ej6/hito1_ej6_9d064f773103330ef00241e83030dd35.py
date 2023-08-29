#Ordenar tres números
# Obtener los números del usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Verificar el orden de los números e intercambiar si es necesario
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1

# Imprimir los números ordenados separados por comas
print("Números ordenados:", num1, ",", num2, ",", num3)
  
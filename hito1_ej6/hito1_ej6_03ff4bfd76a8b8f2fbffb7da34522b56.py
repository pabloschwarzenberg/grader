#Ordenar tres números   
num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))
num3 = int(input("Introduce el tercer número entero: "))
#una lista con los tres números
numeros = [num1, num2, num3]
# lista de menor a mayor
numeros.sort()
# Imprimimos los números ordenados separados por comas
print(numeros[0], ",", numeros[1], ",", numeros[2])

#Ordenar tres números
num1 = int(input("Introduce el primer número entero: "))
2
num2 = int(input("Introduce el segundo número entero: "))
3
num3 = int(input("Introduce el tercer número entero: "))
4
 
5
#una lista con los tres números
6
numeros = [num1, num2, num3]
7
 
8
# lista de menor a mayor
9
numeros.sort()
10
 
11
# Imprimimos los números ordenados separados por comas
12
print(numeros[0], ",", numeros[1], ",", numeros[2])
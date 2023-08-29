1
# Primero, capturamos la entrada del usuario
2
num1 = int(input("Ingresa el primer número: "))
3
num2 = int(input("Ingresa el segundo número: "))
4
num3 = int(input("Ingresa el tercer número: "))
5
 
6
# Luego, los ponemos en una lista
7
numeros = [num1, num2, num3]
8
 
9
# Ordenamos la lista
10
numeros.sort()
11
 
12
# Finalmente, imprimimos los números en orden, separados por comas
13
print(numeros)
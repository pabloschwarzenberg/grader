
# Primero, capturamos la entrada del usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Luego, los ponemos en una lista
numeros = [num1, num2, num3]
 
# Ordenamos la lista
numeros.sort()

# Finalmente, imprimimos los números en orden, separados por comas
print(numeros)
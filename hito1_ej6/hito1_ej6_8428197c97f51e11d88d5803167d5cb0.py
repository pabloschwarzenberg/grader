#Ordenar tres números
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

# Ordenamos los tres números usando una lista temporal
temp = [num1, num2, num3]
temp.sort() # Ordena la lista de menor a mayor

# Imprimimos los números ordenados separados por comas
print(str(temp[0]) + ", " + str(temp[1]) + ", " + str(temp[2]))
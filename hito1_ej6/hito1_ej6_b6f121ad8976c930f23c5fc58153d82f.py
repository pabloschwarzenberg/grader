#Ordenar tres números
# Se solicitan los tres números enteros al usuario
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))

# Se crea una lista con los tres números ingresados
numeros = [numero1, numero2, numero3]

# Se ordena la lista de menor a mayor
numeros.sort()

# Se imprime la lista ordenada separada por comas
print("Los números ordenados de menor a mayor son:", numeros[0], ",", numeros[1], ",", numeros[2])

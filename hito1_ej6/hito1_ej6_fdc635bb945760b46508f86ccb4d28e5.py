#Ordenar tres números
#pedir al usario ingreso de 3 números
numero_1 = int(input("Ingresa el primer número: "))
numero_2 = int(input("Ingresa el primer número: "))
numero_3 = int(input("Ingresa el primer número: "))

#lista con los números ingresados

numeros = [numero_1, numero_2, numero_3]

# Ordenar la lista de menor a mayor
numeros.sort()

# Imprimir los números ordenados separados por comas
print("Los números ordenados de menor a mayor son:", ", ".join(map(str, numeros)))
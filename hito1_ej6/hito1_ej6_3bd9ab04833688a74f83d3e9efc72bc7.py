#Ordenar tres números
 # Solicitar al usuario ingresar los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Ordenar los números de menor a mayor
numeros = sorted([numero1, numero2, numero3])

# Imprimir los números ordenados separados por comas
print("Números ordenados:", ", ".join(str(num) for num in numeros))

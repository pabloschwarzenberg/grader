# Ingresar los tres números enteros
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Ordenar los números de menor a mayor
menor = min(numero1, numero2, numero3)
mayor = max(numero1, numero2, numero3)
medio = (numero1 + numero2 + numero3) - menor - mayor

# Imprimir los números ordenados separados por una coma
print(menor,",",medio,",",mayor)


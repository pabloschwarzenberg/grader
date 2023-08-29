#Ordenar tres números
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

# Ordenar los números de menor a mayor
menor = min(num1, num2, num3)
mayor = max(num1, num2, num3)
medio = (num1 + num2 + num3) - menor - mayor

# Imprimir los números ordenados separados por comas
print("Los números ordenados de menor a mayor: {}, {}, {}".format(menor, medio, mayor))

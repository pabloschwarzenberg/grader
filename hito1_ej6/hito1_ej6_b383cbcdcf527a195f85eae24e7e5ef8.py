# Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.
# Ordenar tres números
n1 = int(input("Ingresa primer número:"))
n2 = int(input("Ingresa segundo número:"))
n3 = int(input("Ingresa tercer número:"))
menor = min(n1, n2, n3)
mayor = max(n1, n2, n3)
medio = n1 + n2 + n3 - menor - mayor
print(menor, ",", medio, ",", mayor)

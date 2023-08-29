#Ordenar tres números
n1 = int(input("Ingrese el primer número entero: "))
n2 = int(input("Ingrese el segundo número entero: "))
n3 = int(input("Ingrese el tercer número entero: "))

menor = min(n1, n2, n3)
mayor = max(n1, n2, n3)
medio = (n1 + n2 + n3) - menor - mayor


print("Números ordenados de menor a mayor:", menor, ",", medio, ",", mayor)
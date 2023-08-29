n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

menor = min(n1, n2, n3)
mayor = max(n1, n2, n3)
medio = n1 + n2 + n3 - menor - mayor

print(str(menor) + ", " + str(medio) + ", " + str(mayor))
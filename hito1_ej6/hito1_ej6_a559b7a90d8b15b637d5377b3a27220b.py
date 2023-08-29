#Ordenar tres números

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

a = max(n1, n2, n3)
b = min(n1, n2, n3)
c = (n1 + n2 + n3) - a - b

print(str(b) + "," + str(c) + "," + str(a))


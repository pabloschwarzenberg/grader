#Ordenar tres números
n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Tercer número: "))

ns = list(sorted([n1, n2, n3]))
print(ns[0], ns[1], ns[2], sep=",")
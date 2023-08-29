#Ordenar tres números
#primero, introducimos los números
n1 = int(input("escribe tu primer número: "))
n2 = int(input("escribe tu segundo número: "))
n3 = int(input("escribe tu tercer número: "))
#introducimos fórmula
z = min(n1, n2, n3)
x = max(n1, n2, n3)
c = (n1 + n2 + n3) - z - x

#concretamos el final
print("Tus números ordenados de menos a mayor equivalen a: {}, {}, {}".format(z, c, x))  
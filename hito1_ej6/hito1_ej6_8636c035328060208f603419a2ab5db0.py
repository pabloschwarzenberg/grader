#Ordenar tres números
p1 = int(input("Ingrese el primer número: "))
p2 = int(input("Ingrese el segundo número: "))
p3 = int(input("Ingrese el tercer número: "))

a = min(p1, p2, p3)
b = max(p1, p2, p3)
c = (p1 + p2 + p3) - a - b

print("Los números ordenados de menor a mayor: {}, {}, {}".format(a, c, b))
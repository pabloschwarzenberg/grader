#Ordenar tres números
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundoo número: "))
c = int(input("Ingrese el tecer número: "))

x = min (a, b, c)
y = max (a, b, c)
z = (a + b + c) - x - y

print (f"\Los números ordenados de menor a mayor son: {x}, {y} y {z}\n")      
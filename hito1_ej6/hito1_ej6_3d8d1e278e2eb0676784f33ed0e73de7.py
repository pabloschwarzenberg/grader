#Ordenar tres números
x = int(input("Escribe el primer número: "))
y = int(input("Escribe el segundo número: "))
z = int(input("Escribe el tercer número: "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

print("Los números son: {}, {}, {}".format(a, b, c))
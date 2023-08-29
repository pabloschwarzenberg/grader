#Ordenar tres números
x = int(input("Escriba el primer número: "))
y = int(input("Escriba el segundo número: "))
z = int(input("Escriba el tercer número: "))

q = min(x, y, z)
w = max(x, y, z)
e = (x + y + z) -q -w

print("El orden de menor a mayor es: {}, {} , {}".format(q, e, w))

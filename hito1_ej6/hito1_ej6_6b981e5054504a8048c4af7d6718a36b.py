#Ordenar tres números
x = int(input("Ingresa el primer digito: "))
y = int(input("Ingresa el segundo digito: "))
z = int(input("Ingresa el tercer digito: "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

print("Los numeros ordenados de menor a mayor son: {}, {}, {}".format(a, b, c))

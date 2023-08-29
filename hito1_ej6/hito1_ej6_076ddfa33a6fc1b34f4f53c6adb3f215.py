a = int(input("Ingresa tu primer numero: "))
b = int(input("Ingresa tu segundo numero: "))
c = int(input("Ingresa tu tercer numero: "))

x = min(a, b, c)
z = max(a, b, c)
y = (a + b + c) - x - z

print("Los numeros ordenados de menor a mayor son: {}, {}, {}".format (x, y, z))
#Ordenar tres números
x = int(input("Ingrese Primer numero: "))
y = int(input("Ingrese Segundo numero: "))
z = int(input("Ingrese Tercer numero: "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

print("Los numeros son: {}, {}, {}" .format(a, b, c))     
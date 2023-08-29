#Ordenar tres números
x =int(input("Esciba el primer numero: "))
y =int(input("Esciba el segundo numero: "))
z =int(input("Esciba el tercer numero: "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

print("Los numero ordenados son: {}, {}, {}". format(a, b, c))
     
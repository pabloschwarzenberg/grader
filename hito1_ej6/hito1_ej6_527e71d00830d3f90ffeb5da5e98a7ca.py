#Ordenar tres números
a = int(input("escriba el primer numero entero: "))
b = int(input("escriba el segundo numero entero: "))
c = int(input("escriba el tercer numero entero: "))

x = min(a, b, c)
y = max(a, b, c)
z = (a + b + c) - x - y

print("{}, {}, {}" .format(x, z, y))
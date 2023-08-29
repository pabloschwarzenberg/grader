x = int(input("escriba el primer numero: "))
y = int(input("escriba el segundo numero: "))
z = int(input("escriba el tercer numero: "))

a = int(min(x, y, z))
c = int(max(x, y, z))
b = int((x + y + z) - a - c)
print("los numeros ordenados son: {}, {}, {}". format(a, b , c))
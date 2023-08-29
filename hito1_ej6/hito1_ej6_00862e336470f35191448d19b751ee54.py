#Ordenar tres números
x = int(input("ingrese el primer numero "))
y = int(input("ingrese el segundo numero "))
z = int(input("ingrese el tercer numero "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c
print("El orden de menor a mayor de los numeros es: {}, {}, {}".format(a, b, c))
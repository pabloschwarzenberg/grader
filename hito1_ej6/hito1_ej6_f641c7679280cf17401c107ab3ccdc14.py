#Ordenar tres números
n1 = int(input("Ingrese el primer numero entero: "))
n2 = int(input("Ingrese el segundo numero entero: "))
n3 = int(input("Ingrese el tercer numero entero: "))

x = min(n1, n2, n3)
y = max(n1, n2, n3)
z = (n1 + n2 + n3) - x - y

print("Los numeros en orden creciente son: {}, {}, {}". format(x, z, y))
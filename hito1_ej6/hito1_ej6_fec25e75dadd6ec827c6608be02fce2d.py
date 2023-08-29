#Ordenar tres números
a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))
c = int(input("Ingresa el tercer numero: "))

x = min (a, b, c)
y = max (a, b, c)
z = (a + b + c) - x - y

print("Numeros ordenados", (x, z, y))
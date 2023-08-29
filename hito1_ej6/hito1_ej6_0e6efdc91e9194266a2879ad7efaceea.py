#Ordenar tres números
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un segundo numero: "))
c = int(input("Ingrese un tercer numero: "))

x = min (a, b, c)
y = max (a, b, c)
z = (a + b + c) - x - y

print ("Numeros ordenados", (x, z, y))
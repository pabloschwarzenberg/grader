#Ordenar tres números de menor a mayor#

a = int(input("Ingrese un numero: "))
b = int(input("Escriba un segundo numero: "))
c = int(input("Escriba un tercer numero: "))

x = min(a, b, c)
y = max(a, b, c)
z = (a + b + c) - x - y

print("Numeros Ordenados", (x, z, y))  
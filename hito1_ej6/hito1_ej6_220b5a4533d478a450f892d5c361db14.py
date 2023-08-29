print("ingrese valores para ordenarlos de menor a mayor")

a = int(input("Ingrese el primer valor :"))
b = int(input("Ingrese el segundo valor :"))
c = int(input("Ingrese el tercer valor :"))

y = max(a, b, c)
x = min(a, b, c)
z = (a+b+c)-x-y
print("el orden de menor a mayor es:", x, ",", z, ",", y)
print("Programa para ordenar tres numeros enteros de menor a mayor")
#datos
x = float(input("Ingrese el primer número: "))
y = float(input("Ingrese el segundo número: "))
z = float(input("Ingrese el tercer número: "))
#calculos
if x < y <= z:
    print(x,y,z)
elif x < z <= y:
    print(x,z,y)
elif y < x <= z:
    print(y,x,z)
elif y < z <= x:
    print(y,z,x)
elif z < x <= y:
    print(z,x,y)
else:
    print(z,y,x)
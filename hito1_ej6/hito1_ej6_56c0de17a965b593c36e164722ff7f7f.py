#Ordenar tres números
x=int(input("Ingrese el primer número entero: "))
y=int(input("Ingrese el segundo número entero: "))
z=int(input("Ingrese el tercer número entero: "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y +z) - a - c

print("Los números ordenados de menor a mayor son: ",a,",",b,",",c)

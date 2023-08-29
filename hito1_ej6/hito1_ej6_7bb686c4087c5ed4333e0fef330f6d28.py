#Ordenar tres números
x = int(input("Escriba un número entero:" ))
y = int(input("Escriba un número entero:" ))
z = int(input("Escriba un número entero:" )) 
a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c
d = (a,b,c)
print("Los números son: " + str(d))
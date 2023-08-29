#Ordenar tres números
x = int(input("Ingrese un numero:"))
y = int(input("Ingrese un numero:"))
z = int(input("Ingrese un numero:"))
a = max(x,z,y)
c = min(x,y,z)
b = (x+y+z) - a - c
print(c,",",b,",",a)
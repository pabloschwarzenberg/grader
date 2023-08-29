print("ejemplo de sistema de ecuacones:")
print("ax+by=c")
print("dx+ey=f")
a=int(input("ingresa un numero (a):"))
b=int(input("ingresa un numero (b):"))
c=int(input("ingresa un numero (c):"))
d=int(input("ingresa un numero (d):"))
e=int(input("ingresa un numero (e):"))
f=int(input("ingresa un numero (f):"))

det = a * e - b * d
x = (e * c - b * f) / det
y = (a * f - d * c) / det

print("el resultado de el sistema de ecuaciones es:")
print("x= ",x)
print("y= ",y)

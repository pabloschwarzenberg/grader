#Sistema de Ecuaciones
a = int(input("ingrese un numero: "))
b = int(input("ingrese un numero: "))
c = int(input("ingrese un numero: "))
d = int(input("ingrese un numero: "))
e = int(input("ingrese un numero: "))
f = int(input("ingrese un numero: "))
g = a * d
h = b * d
i = c * d
j = d * -a
k = e * -a
l = f * -a
y = (i + l) / (h + k)
x = (c - b * y) / a
print("x=", x, "y=", y)
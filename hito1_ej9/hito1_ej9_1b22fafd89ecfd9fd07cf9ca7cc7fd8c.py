#Sistema de Ecuaciones
print("ax + by = c ; dx + ey = f")
print("ingrese los valores de a, b, c, d, e y f")
a = eval(input("a:"))
b = eval(input("b:"))
c = eval(input("c:"))
d = eval(input("d:"))
e = eval(input("e:"))
f = eval(input("f:"))

determinante= a*e - b*d
x = (c*e - b*f)/determinante
y = (a*f - c*d)/determinante
print("x =", x, ", y =", y)      
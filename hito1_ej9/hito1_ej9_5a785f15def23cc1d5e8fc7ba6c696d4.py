#Sistema de Ecuaciones
a = eval(input("ingrese un a:"))
b = eval(input("ingrese un b:"))
c = eval(input("ingrese un c:"))
d = eval(input("ingrese un d:"))
e = eval(input("ingrese un e:"))
f = eval(input("ingrese un f:"))
x = (c*e - b*f)/(a*e - b*d)
y = (a*f - c*d)/(a*e - b*d)
print("x=",x)
print("y=",y)
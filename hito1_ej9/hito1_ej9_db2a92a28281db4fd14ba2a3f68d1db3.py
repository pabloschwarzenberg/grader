#Sistema de Ecuaciones
print("ax + by = c")
print("dx + ey = f")
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
d=float(input("d: "))
e=float(input("e: "))
f=float(input("f: "))
y_a=a*f-d*c
y_b=a*e-d*b
Y=y_a/y_b
x_a=c-b*((a*f-d*c)/(a*e-d*b))
x_b=a
X=x_a/x_b
print("X=",X)
print("Y=",Y)
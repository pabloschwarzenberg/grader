#Sistema de Ecuaciones
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
d=float(input("d="))
e=float(input("e="))
f=float(input("f="))

x=((e*c-b*f)/(a*e-b*d))
y=((a*f-d*c)/(a*e-b*d))

print("x="+ str(x))
print("y="+ str(y))

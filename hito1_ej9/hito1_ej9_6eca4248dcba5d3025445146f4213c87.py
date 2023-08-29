#Sistema de Ecuaciones
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))
e=int(input("e="))
f=int(input("f="))
x=(c*e-b*f)/(a*e-b*d)
y=(a*f-c*d)/(a*e-b*d)
print("x="+str(round(x,1)))
print("y="+str(round(y,1)))


#Sistema de Ecuaciones
x1=float(input(""))
y1=float(input(""))
c1=float(input(""))
x2=float(input(""))
y2=float(input(""))
c2=float(input(""))

x=((y1*c2-y2*c2)/(y1*x2-y2*x1))
x=round(x,1)

y=((x1*c2-x2*c1)/(x1*y2-x2*y1))
y=round(y,1)

print("x=",x)
print("y=", y)
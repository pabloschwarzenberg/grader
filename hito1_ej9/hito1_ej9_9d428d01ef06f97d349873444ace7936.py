print("Resolviendo")
print("ax+by=c")
print("dx+ey=f")
a=float(input("Ingrese a:"))
b=float(input("Ingrese b:"))
c=float(input("Ingrese c:"))
d=float(input("Ingrese d:"))
e=float(input("Ingrese e:"))
f=float(input("Ingrese f:"))
y=(a*f-d*c)/(e*a-d*b)
x=(c-b*y)/a
print("x=",x)
print("y=",y)
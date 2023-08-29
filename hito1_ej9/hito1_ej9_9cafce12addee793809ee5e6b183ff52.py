#Sistema de Ecuaciones

a=float(input(""))
b=float(input(""))
c=float(input(""))
d=float(input(""))
e=float(input(""))
f=float(input(""))


x=(e*c-f*b)//(a*e-d*b)
y=(c-a*((e*c-f*b)//(a*e-d*b)))//b
z=round(y,1)
n=round(x,1)
print("y=",z)
print("x=",n)


#Sistema de Ecuaciones
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
d=int(input("d"))
e=int(input("e"))
f=int(input("f"))

y=(a*f-d*c)/(a*e-d*b)
x=(c-b*y)/a

print("x=",x)
print("y=",y)
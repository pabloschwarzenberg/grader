#Sistema de Ecua
a=float(input("introducir a"))
b=float(input("introducir b"))
c=float(input("introducir c"))
d=float(input("introducir d"))
e=float(input("introducir e"))
f=float(input("introducir f"))

y=(a*f-d*c)/(a*e-b*d)
x=(c-b*y)/a
print("x="+str(x),"y="+str(y))     
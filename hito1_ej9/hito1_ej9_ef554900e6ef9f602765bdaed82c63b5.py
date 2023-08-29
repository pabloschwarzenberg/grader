#Sistema de Ecuaciones
a=int(input("Ingrese valor de a: "))
b=int(input("Ingrese valor de b: "))
c=int(input("Ingrese valor de c: "))
d=int(input("Ingrese valor de d: "))
e=int(input("Ingrese valor de e: "))
f=int(input("Ingrese valor de f: "))
# Resolver "x"
x=((((e*c)/b)-f)/(((e*a)/b)-d))
# Resolver "y"
y=((((d*c)/a)-f)/(((d*b)/a)-e))
# Redondeo
q=round(x,0)
w=round(y,0)
print("x=",q)
print("y=",w)

#Sistema de Ecuaciones
a=int(input("ingresar numero factor de x1:"))
b=int(input("ingresar numero factor de y1:"))
c=int(input("ingresar numero:"))
d=int(input("ingresar numero factor de x2:"))
e=int(input("ingresar numero factor de y2:"))
f=int(input("ingresar numero:")) 
y=(d*c-a*f)/(b*d-e*a)
x=(c*e-f*b)/(a*e-d*b)
print("[","x=",x,",","y=",y,"]")


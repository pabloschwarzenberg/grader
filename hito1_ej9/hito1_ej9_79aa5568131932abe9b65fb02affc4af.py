#Sistema de Ecuaciones
a=0
b=0
c=0
d=0
e=0
f=0
x=0
y=0
z=0
w=0
a=float(input("ingrese el valor x"))
b=float(input("ingrese el valor y"))
c=float(input("ingrese el valor del numero sin variable"))
print("ingresar la segunda ecuacion")
d=float(input("ingrese el valor x"))
e=float(input("ingrese el valor y"))
f=float(input("ingrese el valor del numero sin variable"))
z=(a/d)
w=(b/e)


if z!=w:
    y=((d*c)-(a*f))/(-(e*a)+(b*d))
    x=(c-(b*y))/a
    print("'x="+str(x)+"'"",""y="+str(y)) 
    
     
#Sistema de Ecuaciones
print("Ingrese el valor que desee para cada letra en el sistema de ecuaciones:")
print("ax+by=c")
print("dx+ey=f")

a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

X=((c*e)-(b*f))/((a*e)-(b*d))
Y=((a*f)-(c*d))/((a*e)-(b*d))

print("['x=",round(X,1),"','y=",round(Y,1),"]")
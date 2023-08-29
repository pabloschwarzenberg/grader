#Sistema de Ecuaciones

print("ecuacion 1 : ax+by=c")
print("ecuacion 2 : dx+ey=f")

a=int(input("Ingrese a:",))
b=int(input("Ingrese b:",))
c=int(input("Ingrese c:",))
d=int(input("Ingrese d:",))
e=int(input("Ingrese e:",))
f=int(input("Ingrese f:",))

y=((a*f-c*d)/(a*e-b*d))
x=((c-b*y)/a)

print("x=",round(x,1))
print("y=",round(y,1))     
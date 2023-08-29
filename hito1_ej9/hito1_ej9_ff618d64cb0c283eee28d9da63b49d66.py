#Sistema de Ecuaciones

print ("Resolviendo")
print ("ax+by=c")
print ("dx+ey=f")

a=int(input("Ingrese a: "))
b=int(input("Ingrese b: "))
c=int(input("Ingrese c: "))
d=int(input("Ingrese d: "))
e=int(input("Ingrese e: "))
f=int(input("Ingrese f: "))

y=round((f*a-d*c)/(a*e-d*b),1)
x=round((c-b*y)/a,1)

print ("[x={0},y={1}]".format (x,y))

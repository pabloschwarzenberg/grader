#Sistema de Ecuaciones
a= int(input("Ingresa a: "))
b= int(input("Ingresa b: "))
c= int(input("Ingresa c: "))
d= int(input("Ingresa d: "))
e= int(input("Ingresa e: "))
f= int(input("Ingresa f: "))

print(a,"*x +",b,"*y=",c)
print(d,"*x +",e,"*y=",f)

x= (e*c-b*f)/(a*e-b*d)
y= (a*f-d*c)/(a*e-b*d)

print("x=",x)
print("y=",y)


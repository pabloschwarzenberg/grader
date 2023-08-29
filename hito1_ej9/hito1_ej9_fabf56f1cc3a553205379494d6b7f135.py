#Sistema de Ecuaciones
a=int(input("Elige el valor de la variable a:"))
b=int(input("Elige el valor de la variable b:"))
c=int(input("Elige el valor de la variable c:"))
d=int(input("Elige el valor de la variable d:"))
e=int(input("Elige el valor de la variable e:"))
f=int(input("Elige el valor de la variable f:"))
x=float((c-(f*b/e))/(a-(d*b/e)))
y=float((f-(d*x))/e)

print("x=",x)
print("y=",y)
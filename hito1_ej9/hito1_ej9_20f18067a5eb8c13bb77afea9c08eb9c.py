#Sistema de Ecuaciones
print("ax+by=c")
print("mx+ny=z")

a=int(input("ingrese el valor de a:"))
b=int(input("ingrese el valor de b:"))
c=int(input("ingrese el valor de c:"))
m=int(input("ingrese el valor de m:"))
n=int(input("ingrese el valor de n:"))
z=int(input("ingrese el valor de z:"))

y=round(((a*z)-(m*c))/((a*n)-(b*m)))
x=round((c-(b*y))/a)

print("el valor de x es:",x)
print("el valor de y es:",y)
        
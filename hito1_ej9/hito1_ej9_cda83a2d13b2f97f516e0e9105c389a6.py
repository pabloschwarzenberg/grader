#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())
m=int(input())
n=int(input())
z=int(input())

y=(((a*z)-(m*c))/((a*n)-(b*m)))
x=((c-(b*y))/a)

print("x=",x)
print("y=",y)     
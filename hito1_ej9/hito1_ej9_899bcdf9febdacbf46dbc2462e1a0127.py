#Sistema de Ecuaciones
a=float(input())
b=float(input())   
c=float(input())
d=float(input())
e=float(input())
f=float(input())
discriminante=float(a*e-b*d)
y = ((c*d)-(f*a))/((b*d)-(e*a))
print("y=",y , round,1)

x = (c-(b*y))/a
print("x=",x , round,1)      
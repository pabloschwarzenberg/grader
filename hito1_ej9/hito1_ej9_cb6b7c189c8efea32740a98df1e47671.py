#Sistema de Ecuaciones
a=float(input())
b=float(input())
c=float(input())
p=float(input())
q=float(input())
r=float(input())

x=(c*q-b*r)/(a*q-p*b)
y=(c-(a*(c*q-b*r)/(a*q-p*b)))/b

print("x=",x)
print("y=",y)
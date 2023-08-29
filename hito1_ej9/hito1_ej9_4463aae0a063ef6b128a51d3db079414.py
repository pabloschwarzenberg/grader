#Sistema de Ecuaciones
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
detM=a*e-b*d
x=(c*e-b*f)/detM
y=(a*f-c*d)/detM
print("x=",float(round(x)),sep="")
print("y=",float(round(y)),sep="")
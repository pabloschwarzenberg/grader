#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
y=(d*c-f*a)/(d*b-e*a)
x=(c-b*y)/a
print("x="+str(x))
print("y="+str(y))
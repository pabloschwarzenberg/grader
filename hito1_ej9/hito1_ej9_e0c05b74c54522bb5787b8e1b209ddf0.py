#Sistema de Ecuaciones
a=int(input())    
b=int(input())    
c=int(input())    
d=int(input())    
e=int(input())    
f=int(input())    
g=(a*f-c*d)/(a*e-b*d)
h=(c-b*((a*f-c*d)/(a*e-b*d)))/a
print("x=",h)
print("y=",g)


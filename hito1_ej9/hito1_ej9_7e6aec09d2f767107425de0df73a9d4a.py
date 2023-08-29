#Sistema de Ecuaciones
#ax+by=c  dx+ey=f  
#x=(c-by)/a    x=(f-ey)/d
#igualando se obtiene que y= (af-dc)/(-db+ae) y x= (bf-ec)/(-ea+bd)
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

x=(b*f-e*c)/(-e*a+b*d)
y=(a*f-d*c)/(-d*b+a*e)
print("x=",x)
print("y=",y)
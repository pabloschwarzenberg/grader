#Sistema de Ecuaciones
#sean dos ecuaciones de la forma ax+by=c ^ dx+ey=f
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

#x=(c-by)/a
#x=(f-ey)/d

#d(c-by)=a(f-ey)
#dc-dby=af-fey
#fey-dby=af-dc
#y(fe-db)=af-dc
y=(a*f-d*c)/(f*e-d*b)
x=(c-b*y)/a
print(x)
print(y)


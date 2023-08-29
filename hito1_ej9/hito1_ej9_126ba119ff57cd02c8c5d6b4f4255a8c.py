#Sistema de Ecuaciones
m1=int(input("X1: "))
m2=int(input("Y1: "))
r1=int(input("R1: "))
n1=int(input("X2: "))
n2=int(input("Y2: "))
r2=int(input("R2: "))
m3=m1*n2/m2*-1
m4=m2*n2/m2*-1
r3=r1*n2/m2*-1
m=m3+n1
n=m4+n2
r=r3+r2
x=r/m
y=(r1-(m1*x))/m2
x1=round(x,1)
y1=round(y,1)
lista=[x1,y1]
if x1==-0.0:
  x1=0.0
if y1==-0.0:
  y1=0.0
print("['x=",x1,"','y=",y1,"']")
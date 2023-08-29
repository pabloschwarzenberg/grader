a1=int(input("X1: "))
a2=int(input("Y1: "))
a3=int(input("R1: "))
a4=int(input("X2: "))
a5=int(input("Y2: "))
a6=int(input("R2: "))
m3=a1*a5/a2*-1
m4=a2*a5/a2*-1
r3=a3*a5/a2*-1
m=m3+a4
n=m4+a5
r=r3+a6
x=r/m
y=(a3-(a1*x))/a2
x1=round(x,1)
y1=round(y,1)
lista=[x1,y1]
if x1==-0.0:
  x1=0.0
if y1==-0.0:
  y1=0.0
print("['x=",x1,"','y=",y1,"']")
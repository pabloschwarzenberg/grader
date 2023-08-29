#Sistema de Ecuaciones
x1=float(input())
y1=float(input())
r1=float(input())
x2=float(input())
y2=float(input())
r2=float(input())

alfa1=r1/x1
alfa2=(-y1)/x1

delta1=alfa1*x2
delta2=alfa2*x2

omega1=(-delta1)+r2
omega2=delta2+y2

y=omega1/omega2

beta=r1-y*y1

x=beta/x1
print('x=',round(x,1),'y=',round(y,1))
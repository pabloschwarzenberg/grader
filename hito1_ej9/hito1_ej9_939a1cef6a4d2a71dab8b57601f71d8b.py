#Sistema de Ecuaciones
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
y=(f-d*c/a)/(e-b*d/a)
r=round(y,1)
print("y={0}".format(r))
x=(c-b*(f-d*c/a)/(e-b*d/a))/a
rr=round(x,1)
print("x={0}".format(rr))
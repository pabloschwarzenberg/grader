#Sistema de Ecuaciones
x1 = float(input("X1: "))
y1 = float(input("Y1: "))
r1 = float(input("R1: "))
x2 = float(input("X2: "))
y2 = float(input("Y2: "))
r2 = float(input("R2: "))
y12 = float((-y1)+(y2*x1))
r12 = float(((r2*x1)-r1))
yt = r12/y12
xt = float((r1-(y1*yt))/x1)

print ("x=",round(xt,1))
print ("y=",round(yt,1))     
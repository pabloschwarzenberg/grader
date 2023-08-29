#Sistema de Ecuaciones
x1=float(input("x1: "))
y1=float(input("y1: "))
n1=float(input("n1: "))
x2=float(input("x2: "))
y2=float(input("y2: "))
n2=float(input("n2: "))
yx=y1*x2-y2*x1
nx=n1*x2-n2*x1
xy=x1*y2-x2*y1
ny=n1*y2-n2*y1
ys=nx/yx
xs=ny/xy
print("x=",xs)
print("y=",ys)
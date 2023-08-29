#SISTEMA DE ECUACIONES
print("Ax+By=C")
print("Dx+Ey=F")
x=float(input("ingrese el valor de x en la primera ecuacion:"))
y=float(input("ingrese el valor de y en la primera ecuacion:"))
r=float(input("ingrese el valor de c en la primera ecuacion:"))
x2=float(input("ingrese el valor de x2 en la segunda ecuacion:"))
y2=float(input("ingrese el valor de y2 en la segunda ecuacion:"))
r2=float(input("ingrese el valor de c2 en la segunda ecuacion:"))
n = x * y2 - y * x2
if n != 0:
    x1 = (r * y2 - y * r2) / n
    y1 = (x * r2 - r * x2) / n
print("X=",round(x1, 2))
print("y=",round(y1, 2))
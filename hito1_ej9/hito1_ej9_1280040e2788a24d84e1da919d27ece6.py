x1=float(input("ingrese el primer numero real del primer sistema de ecuaciones: "))   #input("1234")=="1234" float(input("1234"))==1234
y1=float(input("ingrese el segundo numero real del primer sistema de ecuaciones: "))
r1=float(input("ingrese solucion del primer sistema de ecuaciones: "))
x2=float(input("ingrese el primer numero real del segundo sistema de ecuaciones: "))
y2=float(input("ingrese el segundo numero real del segundo sistema de ecuaciones: "))
r2=float(input("ingrese solucion del segundo sistema de ecuaciones: "))
det_sistema=(x1*y2)-(y1*x2)
det_x=(r1*y2)-(y1*r2)
det_y=(x1*r2)-(r1*x2)
x_solucion=(det_x/det_sistema)
y_solucion=(det_y/det_sistema) 
print("x=",round(x_solucion,1))
print("y=",round(y_solucion,1))
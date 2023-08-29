x1 = eval(input("Ingrese X1"))
y1 = eval(input("Ingrese Y1"))
z1 = eval(input("Ingrese Z1"))
x2 = eval(input("Ingrese X2"))
y2 = eval(input("Ingrese Y2"))
z2 = eval(input("Ingrese Z2"))

factor = x2/x1
x1 = x1*factor
y1 = y1*factor
z1 = z1*factor

#x1 == x2
#y1 != y2
#z1 != z2

nuevoY2 = y2 - y1
nuevoZ2 = z2 - z1

#0* X + nuevoY2 * Y = nuevoZ2

yFinal = nuevoZ2 / nuevoY2

#x2*X + y2*Y = z2

xFinal = (z2 - y2*yFinal)/x2

print("x=", round(xFinal,1))

print("y=", round(yFinal,1))





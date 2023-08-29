#Sistema de Ecuaciones
x1 = float(input("Coeficiente de x, primera ecuacion: "))
y1 = float(input("Coeficiente de y, primera ecuacion: "))
c1 = float(input("Resultado 1: "))
x2 = float(input("Coeficiente de x, segunda ecuacion: "))
y2 = float(input("Coeficiente de y, segunda ecuacion: "))
c2 = float(input("Resultado 2: "))
y = ((x2*c1)-(x1*c2))//((x2*y1)-(x1*y2))
x = ((y2*c1)-(y1*c2))//((y2*x1)-(y1*x2))

print ("Y =", y)
print ("X =", x)      
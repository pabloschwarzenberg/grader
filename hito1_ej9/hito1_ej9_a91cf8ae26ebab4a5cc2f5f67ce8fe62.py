#Sistema de Ecuaciones
print("ingrese primera ecuación")
a = float(input("coeficiente de X: "))
b= float(input("coeficiente de Y: "))
c = float(input("ingrese numero libre: "))

print("ingrese segunda ecuación")
a1 = float(input("coeficiente de X: "))
b1= float(input("coeficiente de Y: "))
c1=float(input("ingrese numero libre: "))

determinante = a*b1 -b*a1
if (determinante != 0):
    x =(c*b1 -b * c1)
    y = (a*c1 - a1 * c)
    print("x = {} \n y = {}".format(x,y))
else:
    print("no existe solución")
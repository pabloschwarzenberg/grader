#Sistema de Ecuaciones

print("ingrese primera ecuacion")
a = float(input("Coeficiente de X: "))
b= float(input("Coeficiente de Y: "))
c = float(input("Ingrese numero: "))

print("ingrese segunda ecuacion")
a1 = float(input("Coeficiente de X: "))
b1= float(input("Coeficiente de Y: "))
c1=float(input("Ingrese numero: "))

determinante = a*b1 -b*a1
if (determinante != 0):
    x =(c*b1 -b * c1)
    y = (a*c1 - a1 * c)
    print("x = {} \n y = {}".format(x,y))
else:
    print("No hay solución")
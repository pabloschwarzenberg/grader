#Sistema de Ecuaciones
print("INGRESE PRIMERA ECUACION")
a = float(input("Coeficiente de X: "))
b= float(input("Coeficiente de Y: "))
c = float(input("Ingrese numero libre: "))

print("INGRESE SEGUNDA ECUACION")
a1 = float(input("Coeficiente de X: "))
b1= float(input("Coeficiente de Y: "))
c1=float(input("Ingrese numero libre: "))

determinante = a*b1 -b*a1
if (determinante != 0):
    x =(c*b1 -b * c1)
    y = (a*c1 - a1 * c)
    print("x = {} \n y = {}".format(x,y))
else:
    print("No existe solución")
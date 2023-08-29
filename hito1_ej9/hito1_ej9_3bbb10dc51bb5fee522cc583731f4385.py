#Sistema de Ecuaciones
print("INGRESE 1° ECUACION")
a = float(input("coef. de X: "))
b= float(input("Coef. de Y: "))
c = float(input("Ingrese un numero : "))

print("INGRESE 2° ECUACION")
a1 = float(input("Coef. de X: "))
b1= float(input("Coef. de Y: "))
c1=float(input("Ingrese un numero : "))

determinante = a*b1 -b*a1
if (determinante != 0):
    x =(c*b1 -b * c1)
    y = (a*c1 - a1 * c)
    print("x = {} \n y = {}".format(x,y))
else:
    print("No existe solución")
      
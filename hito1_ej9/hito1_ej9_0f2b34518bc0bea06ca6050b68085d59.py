#Sistema de Ecuaciones
 #Entradas
print("La ecuacion tiene la siguiente forma ax+by=b")

a = float(input("Ingresa el valor a de la ecuacion: "))
b = float(input("Ingresa el valor b de la ecuacion: "))
c = float(input("Ingresa el valor c de la ecuacion: "))

print("La ecuacion tiene la siguiente forma dx+y=0")

d = float(input("Ingresa el valor d de la ecuacion: "))
e = float(input("Ingresa el valor e de la ecuacion: "))
f = float(input("Ingresa el valor f de la ecuacion: "))

#Calculos

if a/d == b/e ==c/f:
    print("Tiene infinitas soluciones")
elif a/b == b/e and a/b != c/f:
    print("No tiene solucion")
else:
    det_s = (a * e) - (b * d)
    det_x = (c * e) - (b * f)
    det_y = (a * f) - (c * d)
    x = round((det_x / det_s),1)
    y = round((det_y / det_s),1)

#Salidas
    print("x=",x)
    print("y=",y)     
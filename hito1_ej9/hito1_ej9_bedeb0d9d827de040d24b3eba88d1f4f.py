#Sistema de Ecuaciones
a1 = eval(input("ingrese a de la primera ecuacion: "))
b1 = eval(input("ingrese b de la primera ecuacion: "))
c1 = eval(input("ingrese c de la primera ecuacion: "))

a2 = eval(input("ingrese a de la segunda ecuacion: "))
b2 = eval(input("ingrese b de la segunda ecuacion: "))
c2 = eval(input("ingrese c de la segunda ecuacion: "))

cambiaA1 = a2 * a1
cambiaB1 = a2 * b1
cambiaC1 = a2 * c1

cambiaA2 = (-1 * a1) * a2
cambiaB2 = (-1 * a1) * b2
cambiaC2 = (-1 * a1) * c2


hallarY = (cambiaC1 + cambiaC2)/(cambiaB1 + cambiaB2)
hallarX = c2 - (b2 * hallarY)

print("x= ",round(hallarX,1))
print("y= ",round(hallarY,1))

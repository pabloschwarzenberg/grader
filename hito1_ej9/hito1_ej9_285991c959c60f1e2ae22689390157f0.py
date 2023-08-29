#Sistema de Ecuaciones
coef1=int(input("ingrese coeficiente de x:"))
coef2=int(input("ingrese coeficiete de y:"))
rec1=int(input("ingrese resultado ecuacion 1:"))
#coef1 y coef2 pertenecen a la primera ecuacion y su resultado

coef3=int(input("ingrese coeficiente de x:"))
coef4=int(input("ingrese coeficinte de y:"))
rec2=int(input("ingrese resultado ecuacion 2:"))
#coef3 y coef4 pertenecen a la segunda ecuacion

y= ((rec2*coef1-coef3*rec1)/(coef4*coef1-coef3*coef2))
x=((rec1-coef2*y)/(coef1))

print("x=",x)
print("y=",y)

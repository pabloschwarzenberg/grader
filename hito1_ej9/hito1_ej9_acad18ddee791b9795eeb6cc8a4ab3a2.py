#Sistema de Ecuaciones
a=float(input("Dime el coeficiente de X de la primera ecuacion:"))
b=float(input("Dime el coeficiente de Y de la primera ecuacion:"))
c=float(input("Dime el resultado de la primera ecuacion:"))
d=float(input("Dime el coeficiente de X de la segunda ecuacion:"))
e=float(input("Dime el coeficiente de Y de la segunda ecuacion:"))
f=float(input("Dime el resultado de la segunda ecuacion:"))
if(a*e-b*d!=0):
  t=((e*(a/d))-b)
  r=(f*(a/d)-c)

  y=(r/t)
  x=((c-(b*y))/a)
  y=round(y, 1)
  x=round(x, 1)
  print("x="+ str(x))
  print("y="+ str(y))

else:print("El sistema de ecuaciones no tiene solucion o tiene infinitas soluciones")


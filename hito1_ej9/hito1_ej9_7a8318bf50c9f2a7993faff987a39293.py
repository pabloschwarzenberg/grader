#Sistema de Ecuaciones
a1=float(input("Ingrese el termino x de la primera ecuacion: "))
a2=float(input("Ingrese el termino y de la primera ecuacion: "))
a3=float(input("Ingrese la igualdad de la primera ecuacion: "))
b1=float(input("Ingrese el termino x de la segunda ecuacion: "))
b2=float(input("Ingrese el termino y de la segunda ecuacion: "))
b3=float(input("Ingrese la igualdad de la segunda ecuacion: "))
#Aqui añado el determinante
d=a1*b2-a2*b1
if d!=0:
  x=(b2*a3-a2*b3)/d
  y=(a1*b3-b1*a3)/d
  print("La solución al sistema es x=",x,"e y=",y)
else:
  print("El sistema tiene infinitas o ninguna solución")
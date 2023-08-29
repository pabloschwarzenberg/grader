#Sistema de Ecuaciones
x1 = int(input("Ingrese N de la primera x: "))
y1 = int(input("Ingrese N de la primera y: "))
valor1 = int(input("Ingrese el valor de la primera ecuacion: "))
x2 = int(input("Ingrese N de la segunda x: "))
y2 = int(input("Ingrese N de la segunda y: "))
valor2 = int(input("Ingrese el valor de la segunda ecuacion: "))

doblex2 = 2*x2
dobley2 = 2*y2
doblevalor2 = 2*valor2

valory = float((valor1-doblevalor2)/(y1-dobley2))
valorx = float((valor1-(y1*valory))/x1)
print("x=",valorx,"y=",valory)     
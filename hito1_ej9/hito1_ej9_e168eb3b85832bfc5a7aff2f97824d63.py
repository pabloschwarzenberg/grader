#Sistema de Ecuaciones
import numpy

x1=int(input("ingrese numero: "))
y1=int(input("ingrese numero: "))
r1=int(input("ingrese numero: "))
x2=int(input("ingrese numero: "))
y2=int(input("ingrese numero: "))
r2=int(input("ingrese numero: "))
A = numpy.array([[x1, y1], [x2, y2]])
B = numpy.array([r1, r2])
X = numpy.linalg.inv(A).dot(B)

valor_x= X[0]
valor_y= X[1]
print("x=",valor_x)
print("y=",valor_y)        
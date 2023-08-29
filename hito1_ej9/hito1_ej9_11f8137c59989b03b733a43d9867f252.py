#Sistema de Ecuaciones
a = int(input('Ingrese A= '))
b = int(input('Ingrese B= '))
c = int(input('Ingrese C= '))
d = int(input('Ingrese D= '))
e = int(input('Ingrese E= '))
f = int(input('Ingrese F= '))
det = a * e - b * d
x= (c * e - b * f) / det
y = (a * f - d * c) / det
print('x=',x)
print('y=',y)
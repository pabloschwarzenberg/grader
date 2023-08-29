from math import sqrt
a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
if a != 0:
x=(-b/a)
print ('Solucion de la ecuacion: x=%4.3f  ' % (x))
else:
if  a == 0 and  b != 0:
print ('la ecuacion no tiene solucion:')
else:
print ('La ecuacion tiene infinitas soluciones. ')
#Sistema de Ecuaciones
a = int(input('Ingrese numero '))
b = int(input('Ingrese numero '))
c = int(input('Ingrese numero '))
d = int(input('Ingrese numero '))
e = int(input('Ingrese numero '))
f = int(input('Ingrese numero '))
sistema = [[a*-d, b*-d, c*-d],
           [d*a, e*a, f*a]]
sistema2 = [sistema[0][0] + sistema[1][0], sistema[0][1] + sistema[1][1], sistema[0][2] + sistema[1][2]]
y = (sistema[0][2] + sistema[1][2])/(sistema[0][1] + sistema[1][1])
x = f - (e * y)
print('x = ', x,'\n','y = ', y)    
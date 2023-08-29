a = float(input('Ingrese numeros: '))
b = float(input('Ingrese numeros: '))
c = float(input('Ingrese numeros: '))
a2 = float(input('Ingrese numeros: '))
b2 = float(input('Ingrese numeros: '))
c2 = float(input('Ingrese numeros: '))

determinante = (a2*b) - (a*b2)
determinanteX = (c2*b) - (c*b2)
determinanteY = (c*a2) - (c2*a)
x= determinanteX / determinante
y = determinanteY / determinante

print('x=' + str(x))
print('y=' + str(y))
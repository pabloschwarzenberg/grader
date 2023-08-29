#Sistema de Ecuaciones
x1 = int(input('ingrese x1: '))
y1 = int(input('ingrese y1: '))
z1 = int(input('ingrese z1: '))
x2 = int(input('ingrese x2: '))
y2 = int(input('ingrese y2: '))
z2 = int(input('ingrese z2: '))


const = x1/x2
valor_y = y1 - (y2 * const)
valor_libre = z1 - (z2 * const)
res_y = valor_libre/valor_y



valor_x = (z1 - (y1*res_y)) / x1

print('x=' + str(valor_x))
print('y=' + str(res_y))

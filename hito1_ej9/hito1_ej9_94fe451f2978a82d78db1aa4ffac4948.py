#Sistema de Ecuaciones
x1 = int(input('\nX1: '))
y1 = int(input('Y1: '))
r1 = int(input('R1: '))
x2 = int(input('X2: '))
y2 = int(input('Y2: '))
r2 = int(input('R2: '))

y = round(((r1*-x2)+(r2*x1))/((y1*-x2)+(y2*x1)), 1)
x = round(((r1*-y2)+(r2*y1))/((x1*-y2)+(x2*y1)), 1)

print('x=', x)
print('y=', y)
#Sistema de Ecuaciones
a, b, c, d, e, f = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())

y = (f*a - c*d) / (a*e- d*b)
x = (c - b*y) / a

print('''x={}
y={}'''.format(x, y))
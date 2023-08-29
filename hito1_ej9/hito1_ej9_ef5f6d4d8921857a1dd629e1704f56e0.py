#Sistema de Ecuaciones
a = float(input('Ingrese número: '))
b = float(input('Ingrese número: '))
c = float(input('Ingrese número: '))
a_ = float(input('Ingrese número: '))
b_ = float(input('Ingrese número: '))
c_ = float(input('Ingrese número: '))

y = (a_ * c - a * c_) / (a_ * b - a * b_ )
x = (c - b * y) / a

print('x=', round(x, 1))
print('y=', round(y, 1))
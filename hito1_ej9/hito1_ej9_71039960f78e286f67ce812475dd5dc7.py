#Sistema de Ecuaciones
print("ax bx c")
print("dx ex f")
a = float(input('Ingrese a: '))
b = float(input('Ingrese b: '))
c = float(input('Ingrese c: '))
d = float(input('Ingrese d: '))
e = float(input('Ingrese e: '))
f = float(input('Ingrese f: '))


detSis = (a*e)-(d*b)
detx = (c*e)-(b*f)
dety = (a*f) - (c*d)

x = detx/detSis
y = dety/detSis

print('x=',x)
print('y=',y)
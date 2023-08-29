#Sistema de Ecuaciones
print('Para las ecuaciones "ax + by = c" y "dx + ey = f", ingresa a, b, c, d, e y f')

a=int(input('Ingresa el valor de la constante a: '))
b=int(input('Ingresa el valor de la constante b: '))
c=int(input('Ingresa el valor de la constante c: '))
d=int(input('Ingresa el valor de la constante d: '))
e=int(input('Ingresa el valor de la constante e: '))
f=int(input('Ingresa el valor de la constante f: '))


x=(f-e*c/b)/(d-a*e/b)
y=c/b - (a/b)*x

print('x= ',x)

print('y= ', y)      
#Sistema de Ecuaciones
print('** SISTEMA DE ECUACIONES **')

print('-- Primera ecuacuión:')
a = int(input())
b = int(input())
c = int(input())
print('-- Segunda ecuacuión:')
d = int(input())
e = int(input())
f = int(input())

y = ((f*a)-(d*c))/((e*a)-(d*b))
x = ((b*f)-(e*c))/((b*d)-(e*a))

print('x='+str(x))
print('y='+str(y))
#Nota final
pt=eval(input('Indique nota de tareas: '))
pi=eval(input('Indique nota de interrogaciones: '))
ne=eval(input('Indique nota de examen: '))
pp=eval(input('Indique nota de presentacion: '))
if pt<1 or pi<1 or ne<1 or pp<1:
    print('Todos los valores tienen que ser mayores o iguales a 1')
elif pt>7 or pi>7 or ne>7 or pp>7:
    print('Todos los valores tienen que ser menores o iguales a 7')
else:
    print('Tu promedio final es: ', ((0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)))      
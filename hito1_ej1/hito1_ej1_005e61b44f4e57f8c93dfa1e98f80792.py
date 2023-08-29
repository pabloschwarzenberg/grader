#Nota final
print('Ingrese las siguientes calificaciones para obtener el promedio final')
pt=float(input('Ingrese la nota correspondiente a tareas: '))
pi=float(input('Ingrese la nota correspondiente a interrogaciones: '))
ne=float(input('Ingrese la nota correspondiente a examen: '))
pp=float(input('Ingrese la nota correspondiente a presentación: '))

pf=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)

print('El promedio final es : ', pf)
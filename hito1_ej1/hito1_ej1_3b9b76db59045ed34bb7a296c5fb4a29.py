#Nota final
print('Ingrese sus cuatro notas para calcular la nota final.')

PT=eval(input('Ingrese su nota de Tareas: '))
PI=eval(input('Ingrese su nota de las Interrogaciones: '))
NE=eval(input('Ingrese su nota del Examen: '))
PP=eval(input('Ingrese su nota de la Presentacion: '))

notafinal=0.3*PT+0.3*PI+0.3*NE+0.1*PP

if 7>=PT>=1 and 7>=PI>=1 and 7>=NE>=1 and 7>=PP>=1:
    print('Su promedio final es: ',round(notafinal,1))
else:
    print('ERROR, Ingrese una nota valida.')
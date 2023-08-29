#Nota final
print('Bienvienido, ingrese sus notas porfavor: ')
PT = float(input('Ingrese el promedio de sus Tareas: '))
PI = float(input('Ingrese su nota de interrogaciones: '))
NE = float(input('Ingrese su nota de Examen: '))
PP = float(input('Ingrese Nota Presentacion: '))
final=(.3*PT)+(.3*PI)+(.3*NE)+(.1*PP)
print('Su nota final es: ',"{0:.1f}".format(final))
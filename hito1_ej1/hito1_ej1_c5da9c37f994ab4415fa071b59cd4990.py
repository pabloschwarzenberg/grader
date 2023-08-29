#Nota final
print('Ingrese sus 4 notas')
pt = float(input('Ingrese nota en Tareas: '))
pi = float(input('Ingrese nota en Interrogaciones: '))
ne = float(input('Ingrese nota Examen: '))
pp = float(input('Ingrese nota Presentacion: '))

x = round((0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp),1)
print('Su promedio es: ', x)
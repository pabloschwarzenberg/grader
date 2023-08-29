#Nota final
pt = float(input('Ingrese la nota de tareas: '))
pi = float(input('Ingrese la nota de interrogaciones: '))
ne = float(input('Ingrese la nota de examen: '))
pp = float(input('Ingrese la nota de presentacion: '))
promedio_final = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
print('El promedio final es: ', round(promedio_final, 1))

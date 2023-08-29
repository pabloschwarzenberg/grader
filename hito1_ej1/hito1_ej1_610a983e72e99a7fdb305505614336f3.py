#Nota final
PT=float(input('notas de tareas: '))
PI=float(input('notas de interrogaciones: '))
NE=float(input('notas de examen: '))
PP=float(input('nota de presentacion: '))

promedio=round(0.3*PT+0.3*PI+0.3*NE+0.1*PP,1)
print('el promedio final es: ',promedio)
#Nota final
PT=eval(input('Ingresa tu promedio de tareas (nota): '))
PI=eval(input('Ingresa tu promedio de interrogaciones (nota): '))
NE=eval(input('Ingresa tu nota de examen (nota): '))
PP=eval(input('Ingresa tu promedio de presentacion (nota): '))

sumapromedio=0.3*PT+0.3*PI+0.3*NE+0.1*PP
print(round(sumapromedio, 1))
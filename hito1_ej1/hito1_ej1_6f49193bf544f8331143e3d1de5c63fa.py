#Nota final
pt=float(input('Ingrese la nota de su tarea: '))
pi= float(input('Ingrese la nota de su interrogacion: '))
ne= float(input('Ingrese la nota de su examen: '))
pp= float(input('Ingrese la nota de su presentacion: '))

promedio=((0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp))
promedio_redondeado = round(promedio, 1)

print("El promedio final es:", promedio_redondeado)
#Nota final
Tareas = float(input('Ingrese el promedio de las tareas: '))
Interrogaciones = float(input('Ingrese el promedio de las Interrogaciones: '))
Examen = float(input('Ingrese el promedio del Examen: '))
Presentacion = float(input('Ingrese el promedio de la presentacion: '))
PT = Tareas
PI = Interrogaciones
NE= Examen
PP = Presentacion
resultado=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
result= round(resultado,1)
print('El promedio final es: ', result)

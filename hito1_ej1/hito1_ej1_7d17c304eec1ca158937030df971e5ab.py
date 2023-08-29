#Nota final
Tarea=float(input('Ingrese el promedio de sus tareas: '))
print('')
Interrogaciones=float(input('Ingrese el promedio de sus interrogaciones: '))
print('')
Examen=float(input('Ingrese la nota de su examen: '))
print('')
Presentacion=float(input('Ingrese la nota de su presentacion: '))
print('')
NotaFinal=(Tarea*0.3)+(Interrogaciones*0.3)+(Examen*0.3)+(Presentacion*0.1)

print('')
print('Su nota final es: '+str(round(NotaFinal,1)))  
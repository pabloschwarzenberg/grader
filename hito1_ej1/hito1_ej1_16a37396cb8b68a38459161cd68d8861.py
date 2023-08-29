#Nota final
notaTareas = float(input('Ingrese la nota de las tareas: '))
notaInterrogaciones = float(input('Ingrese la nota de las Interrogaciones: '))
notaExamen = float(input('Ingrese la nota del Examen: '))
notaPresentacion = float(input('Ingrese la nota de Presentacion: '))

promedioFinal = (0.3 * notaTareas) + (0.3 * notaInterrogaciones) + (0.3 * notaExamen) + (0.1 * notaPresentacion)
print(f'El promedio Final es: {promedioFinal:.1f}')
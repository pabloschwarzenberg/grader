tareas = eval(input('Ingrese el PT: '))
interrogacion = eval(input('Ingrese el PI: '))
examen = eval(input('Ingrese el NE: '))
presentacion = eval(input('Ingrese el PP: '))

resultadoTareas = 0.3 * tareas
resultadoInterrogacion = 0.3 * interrogacion
resultadoExamen = 0.3 * examen
resultadoPresentacion = 0.1 * presentacion

resultadoFinal = (resultadoTareas + resultadoInterrogacion + resultadoExamen + resultadoPresentacion) * 10

if resultadoFinal % int(resultadoFinal) > 0.4:
    resultadoFinal = (int(resultadoFinal) + 1) / 10
else:
    resultadoFinal = int(resultadoFinal) / 10

print(resultadoFinal)
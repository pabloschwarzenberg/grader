#Nota final
notaTareas = eval(input("Ingresa la nota de Tareas: "))
notaInterrogaciones = eval(input("Ingresa la nota de Interrogaciones: "))
notaExamen = eval(input("Ingresa la nota de Exámen: "))
notaPresentacion = eval(input("Ingresa la nota de Presentación: "))
notaFinal = (0.3 * notaTareas) + (0.3 * notaInterrogaciones) + (0.3 * notaExamen) + (0.1 * notaPresentacion)
print(notaFinal)
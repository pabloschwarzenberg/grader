PT = float(input('ingresa notas tareas: '))
PI = float(input('ingresa notas interrogaciones: '))
NE = float(input('ingresa notas examen: '))
PP = float(input('ingresa notas presentacion: '))
notaFinal = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print('la nota final es: ', notaFinal)
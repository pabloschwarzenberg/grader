#Nota final
PT = eval(input('Ingresa nota de tarea: '))
PI = eval(input('Ingresa nota de evaluaciones: '))
NE = eval(input('Ingresa nota de examen: '))
PP = eval(input('Ingresa nota de presentación: '))

Promedio = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)

print ('promedio es: ',round(Promedio,1))
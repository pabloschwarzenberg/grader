PT = float(input('Ingrese la nota de sus tareas: '))
PI = float(input('Ingrese la nota de sus interrogaciones: '))
NE = float(input('Ingrese la nota de su examen: '))
PP = float(input('Ingrese la nota de su presentación: '))

PT *= 0.3
PI *= 0.3
NE *= 0.3
PP *= 0.1
promedio = (PT+PI+NE+PP)
promedio = round(promedio, 1)

print('Su promedio final es: ', promedio)
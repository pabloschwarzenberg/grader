#Nota final
PT = float(input('Tareas: '))
PI = float(input('interrogaciones: '))
NE = float(input('Examen: '))
PP = float(input('Presentación: '))

promedio = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
promedio = round(promedio, 1)

print(promedio)
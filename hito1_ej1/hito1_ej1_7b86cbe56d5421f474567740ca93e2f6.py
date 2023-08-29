#Nota final
PT = float(input('Por favor, ingresa tu nota de tareas: '))
PI = float(input('Por favor, ingresa tu nota de interrogaciones: '))
NE = float(input('Por favor, ingresa tu nota de examen: '))
PP = float(input('Por favor, ingresa tu nota de presentación: '))

notapromedio = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
print(round(notapromedio, 1))
#Nota final
PT = float(input('Ingrese el promedio de notas de las tareas: '))
PI = float(input('Ingrese el promedio de notas de las interrogaciones: '))
NE = float(input('Ingrese la nota de su examen: '))
PP = float(input('Ingrese la nota de presentación: '))

PR_F = round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP, 1)

print(PR_F)
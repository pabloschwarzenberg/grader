#Nota final


PT = float(input('Ingrese el promedio de nota de sus Tareas: '))
PI = float(input('Ingrese el promedio de nota de sus Interrogaciones: '))
NE = float(input('Ingrese su nota de examen: '))
PP = float(input('Ingrese su nota de presentacion: '))

promedioFinal = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print(round(promedioFinal,1))
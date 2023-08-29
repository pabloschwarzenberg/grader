#Nota final
PT = float(input('Ingrese la nota de las tareas: '))
PI = float(input('Ingrese la nota de las Interrogaciones: '))
NE = float(input('Ingrese la nota del Examen: '))
PP = float(input('Ingrese la nota de Presentacion: '))
PromedioFinal = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
PromedioFinal = round(PromedioFinal, 1)
print(PromedioFinal)
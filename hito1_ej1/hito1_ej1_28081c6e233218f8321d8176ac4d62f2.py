#PT = Tareas
#PI = Interrogaciones
#NE = Examen
#PP = Presentacion

PT = float(input('Ingrese la nota de Tareas: '))
PI = float(input('Ingrese la nota de Interrogaciones: '))
NE = float(input('Ingrese la nota del Examen: '))
PP = float(input('Ingrese la nota de Presentacion: '))

suma = PT + PI + NE + PP
prom = suma / 4
print("El promedio de notas es: ",prom)
print(round(prom,1))
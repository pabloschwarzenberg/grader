PT = float(input('Por favor, introduzca la nota de las tareas: '))
PI = float(input('Por favor, introduzca la nota de las interrogaciones: '))
NE = float(input('Por favor, introduzca la nota del examen: '))
PP = float(input('Por favor, introduzca la nota de la presentacion: '))

NF = (0.3*PT)+(PI*0.3)+(NE*0.3)+(PP*0.1)

print(round(NF, 1))
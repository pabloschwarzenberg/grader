#Nota final
PT = float(input('Introduce nota de tareas: '))
PI = float(input('Introduce nota de interrogaciones: '))
NE = float(input('Introduce nota de examen: '))
PP = float(input('Introduce nota de presentacion: '))

NF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

print('La nota final es' + str(NF) )
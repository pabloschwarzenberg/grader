#Nota final
n1 = float(input('Ingrese la nota de Tareas: '))
n2 = float(input('Ingrese la nota de Interrogaciones: '))
n3 = float(input('Ingrese la nota de Examen: '))
n4 = float(input('Ingrese la nota de Presentacion: '))

PT = n1 * 0.3
PI = n2 * 0.3
NE = n3 * 0.3
PP = n4 * 0.1

nota_final = PT + PI + NE + PP
print(round(nota_final, 1))
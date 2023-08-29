#Nota final
PT = float(input('Ingresa la nota de tareas: '))
PI = float(input('Ingresa la nota de interrogaciones: '))
NE = float(input('Ingresa la nota de examen: '))
PP = float(input('Ingresa la nota de presentacion: '))
Notas = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
Redondeo = round(Notas, 1)
print(Redondeo)
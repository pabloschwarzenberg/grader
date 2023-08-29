#Nota final
PT=float(input('ingresar nota de la tarea: '))
PI=float(input('ingresar nota de interrogaciones: '))
NE=float(input('ingresar nota de examen: '))
PP=float(input('ingresar nota de Presentacion: '))

nota=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print(round(nota,1))


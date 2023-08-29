#Nota final
PT = float(input('Ingrea la nota de tu Tarea: '))
PI = float(input('Ingresa la nota de tu Interrogacion: '))
NE = float(input('Ingresa la nota de tu Examen: '))
PP = float(input('Ingresa la nota de tu Presentacion: '))

NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(round(NF, 1))

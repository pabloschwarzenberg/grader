#Nota finalPT = float(input('ingrese la nota de las tareas: '))
PT = float(input('ingrese la nota de las tareas: '))
PI = float(input('ingrese la nota de las interrogaciones: '))
NE = float(input('ingrese la nota del examen: '))
PP = float(input('ingrese la nota de presentacion: '))

NF = round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP, 1)
print(NF)
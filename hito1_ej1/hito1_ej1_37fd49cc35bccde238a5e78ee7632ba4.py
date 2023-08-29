print('ingrese las siguientes notas')
PT = int(input('Tareas: '))
PI = int(input('Interrogaciones: '))
NE = int(input('Examen: '))
PP = int(input('Presentaciones: '))
Promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
PF = round(Promedio,1)
print(PF)
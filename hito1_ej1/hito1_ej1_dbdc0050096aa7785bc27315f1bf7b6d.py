#Nota final
PT = float(input('Nota de tareas: '))
PI = float(input('Nota de Interrogaciones: '))
NE = float(input('Nota de examen: '))
PP = float(input('Nota de presentacion: '))

calculo = 0.3*PT+0.3*PI+0.3*NE+0.1*PP
print(round(calculo,1))      
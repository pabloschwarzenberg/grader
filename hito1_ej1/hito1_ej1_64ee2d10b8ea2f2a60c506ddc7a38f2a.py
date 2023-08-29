#Nota final

PT = float(input('Ingrese nota tareas:'))
PI = float(input('Ingrese nota interrogación:'))
NE = float(input('Ingrese nota examen:'))
PP = float(input('Ingrese nota presentación:'))
Formula = 0.3*PT+0.3*PI+0.3*NE+0.1*PP
print(round(Formula, 1))
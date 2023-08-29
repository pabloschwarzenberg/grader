#Nota final
PT = float(input('Ingrese la nota de las tareas: ') )
PI = float(input('Ingrese la nota de las interrogaciones: ') )
NE = float(input('Ingrese la nota del examen: ') )
PP = float(input('Ingrese la nota de la presentación: ') )
promedio_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print('El promedio final es: ' + str(round(promedio_final, 1)))  
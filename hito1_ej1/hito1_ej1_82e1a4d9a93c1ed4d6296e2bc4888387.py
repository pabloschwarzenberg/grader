#Nota final    
print('Ingrese las siguientes notas:')
PT = float(input('Tareas: '))
PI = float(input('Interrogaciones: '))
NE = float(input('Examen: '))
PP = float(input('Presentación: '))
promedio = round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP, 1)
print('Su promedio final es:', promedio)

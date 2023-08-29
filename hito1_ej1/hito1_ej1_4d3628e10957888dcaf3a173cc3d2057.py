#Nota final
PT = float(input('Ingresa nota de Tareas'))
PI = float(input('Ingresa nota de Interrogaciones'))
NE = float(input('Ingresa nota de Examen'))
PP = float(input('Ingresa nota de Presentacion'))
nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print('El promedio final es: ', nota_final)
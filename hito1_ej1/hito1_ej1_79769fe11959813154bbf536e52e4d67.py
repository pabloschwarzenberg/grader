#Nota final
PT = float(input("introduce tu nota de tareas:"))
PI = float(input("introduce tu nota de interrogaciones:"))
NE = float(input("introduce tu nota del examen:"))
PP = float(input("introduce tu nota de presentaciones:"))
#Proceso
promedio_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
#Salida
print("el promedio_final es:",round(promedio_final,1))
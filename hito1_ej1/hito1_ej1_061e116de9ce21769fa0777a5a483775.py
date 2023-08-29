#Nota final
PT = float(input("nota de Tareas"))
PI = float(input("nota de Interrogaciones"))
NE = float(input("nota de Examen"))
PP = float(input("nota de Presentacion"))
promedio =  0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(round(promedio,1))
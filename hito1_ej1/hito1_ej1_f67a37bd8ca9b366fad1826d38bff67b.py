#Nota final
PT = float(input("Notas de Tareas"))
PI = float(input("Notas de Interrogaciones"))
NE = float(input("Notas de Examen"))
PP = float(input("Notas de Presentacion"))
Notas_Promedio= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
NotasFinal= round(Notas_Promedio, 1)
print(NotasFinal)  
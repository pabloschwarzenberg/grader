#Nota final
PT = float(input("Indique la nota de las TAREAS: "))
PI = float(input("Indique la nota de las INTERROGACIONES: "))
NE = float(input("Indique la nota del EXAMEN: "))
PP = float(input("Indique la nota de la PRESENTACIÓN: "))
prom = 0.3* PT + 0.3*PI + 0.3*NE + 0.1*PP
print("Su nota final es:",round(prom,1))    
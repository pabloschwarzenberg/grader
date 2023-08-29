#Nota final
PT = float(input("Ingrese sus notas de tareas:"))
while PT > 7:
    PT = float(input("Ingrese sus notas de tareas:"))

PI = float(input("Ingrese sus notas de interrogaciones:"))
while PI > 7:
    PI = float(input("Ingrese sus notas de interrogaciones:"))
NE = float(input("Ingrese sus notas de examen:"))
while NE > 7:
    NE = float(input("Ingrese sus notas de examen:"))

PP = float(input("Ingrese sus notas de presentacion:"))
while PP > 7:
    PP = float(input("Ingrese sus notas de presentacion:"))

PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("Su promedio final es " + str(round(PF, 1)))      
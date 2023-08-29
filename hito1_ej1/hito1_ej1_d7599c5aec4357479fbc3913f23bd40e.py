#Nota final
PT = eval(input(" Ingrese nota de tareas: "))
PI = eval(input(" Ingrese nota de interrogaciones: "))
NE = eval(input(" Ingrese nota de examen: "))
PP = eval(input(" Ingrese nota de Presentación: "))
PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
PFR = round(PF,1)
print("El promedio del ramo es: ",PFR)   
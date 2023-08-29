PT = eval(input("Ingrese nota de Tareas:"))
PI = eval(input("Ingrese nota de Interrogaciones:"))
NE = eval(input("Ingrese nota de Examen:"))
PP = eval(input("Ingrese nota de Presentacion:"))
PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
PFR = round(PF,1)
print ("Promedio Final=",PFR)

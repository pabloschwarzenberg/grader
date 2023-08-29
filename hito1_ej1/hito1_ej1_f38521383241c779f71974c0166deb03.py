#Nota final
PT = float(input("Ingrese nota de Tareas:"))
PI = float(input("Ingrese nota de Interrogacion:"))
NE = float(input("Ingrese nota de Examen:"))
PP = float(input("Ingrese nota de Presentacion:"))
PF = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("El promedio final del estudiante es:")
print(round(PF,1))
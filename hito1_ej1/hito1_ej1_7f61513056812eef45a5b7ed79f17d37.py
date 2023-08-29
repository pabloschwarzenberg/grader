#Nota final
PT= float(input("Ingrese promedio de Tareas: "))
PI=float(input("Ingrese promedio de Interrogaciones: "))
NE=float(input("Ingrese nota de Examen: "))
PP=float(input("Ingrese promedio de Presentacion: "))
NF= (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
NF= round(NF,1)
print(NF) 
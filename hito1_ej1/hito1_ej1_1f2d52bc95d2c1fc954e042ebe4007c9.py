#Nota Final
print("Calculo de Promedio Final Alumno")
PT=float(input("Ingresar Nota de Tareas: "))
PI=float(input("Ingresar Nota de Interrogaciones: "))
NE=float(input("Ingresar Nota de Examen: "))
PP=float(input("Ingresar Nota de Presentación: "))
NF=float(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print(round(NF,1))
#Nota final
PT = float(input("Ingrese promedio tareas: "))
PI = float(input("ingrese promedio interrogaciones: "))
NE = float(input("ingrese nota examen: "))
PP = float(input("ingrese promedio presentacion: "))
PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
resultado_redondeado = round(PF, 1)
print("el promedio final es: ", resultado_redondeado)      
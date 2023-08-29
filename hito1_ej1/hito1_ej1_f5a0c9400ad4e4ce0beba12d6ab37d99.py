#Nota final
print("--ingrese sus notas--")

PT = float(input("Ingrese su nota de tareas: "))
PI = float(input("Ingrese nota de interrogaciones: "))
NE = float(input("Ingrese nota de Examen: "))
PP = float(input("Ingrese nota de Presentación: "))

PR = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
PR2 = round(PR,1)
print("su nota final es: ", PR2)    
#Nota final
PT = float(input("ingrese promedio de tareas: \n"))
PI = float(input("ingrese promedio de interrogaciones: \n"))
NE = float(input("ingrese nota examen: \n"))
PP = float(input("ingrese nota presentación: \n"))
Nota_Final = 0.3*PT + 0.3*PI +0.3*NE + 0.1*PP
print("La nota final del curso es: " + str(Nota_Final))
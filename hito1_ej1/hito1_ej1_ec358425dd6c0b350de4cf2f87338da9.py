#Nota final
PT = float(input("ingrese nota de tareas:  "))
PI = float(input("ingrese nota de interrogaciones: "))
NE = float(input("ingrese nota de examen: "))
PP = float(input("ingrese nota de presentacion: "))
NT = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("La nota final del curso es : ", round(NT,1))

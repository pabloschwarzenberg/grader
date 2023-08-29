#Nota final

PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de interrogaciones: "))
NE = float(input("Ingrese la nota del examen: "))
PP = float(input("Ingrese nota de las presentaciones : "))

NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("La NF del curso es: ", round(NF,1))      
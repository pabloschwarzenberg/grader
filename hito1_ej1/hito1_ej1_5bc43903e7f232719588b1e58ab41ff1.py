#Nota final
PT = float(input("Introduce la nota de tareas: "))
PI = float(input("Introduce la nota de interrogaciones: "))
NE = float(input("Introduce la nota de examen: "))
PP = float(input("Introduce la nota de presentacion: "))
print("El promedio final es: ", round((0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP),1))      
PT = float(input("Ingrese nota de tareas: "))
PI = float(input("Ingrese interrogaciones: "))
NE= float(input("Ingrese notas de examen: "))
PP = float(input("Ingrese nota de presentacion: "))

formula = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP


print("El promedio final es: ", formula)
#Nota final
PT = float(input(" Ingrese Nota de Tareas: "))
PI = float(input(" Ingrese Nota de Interrogaciones: "))
NE = float(input("Ingrese Nota de Examen: "))
PP = float(input("Ingrese Nota de Presentacion: "))

R = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

print("Su Nota final es: ", "{:.1f}".format(R))      
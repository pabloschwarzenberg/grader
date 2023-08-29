PT = float(input("Ingrese nota de tareas: "))
PI = float(input("Ingrese nota de interrogaciones: "))
NE = float(input("Ingrese nota de examenes: "))
PP = float(input("Ingrese nota de presentacion: "))

PF =  0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("su promedio final", round(PF, 1 ))
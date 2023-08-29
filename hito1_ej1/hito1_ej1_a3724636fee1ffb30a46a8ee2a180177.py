#Nota final
PT = float(input("Ingrese nota de tareas: "))
PI = float(input("Ingrese nota de interrogaciones: "))
NE = float(input("Ingrse nota de examen: "))
PP = float(input("Ingrese nota de presentaciones: "))
PF = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print("Usuaria (o) su promedio final es: ", round(PF,1))
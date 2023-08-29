#Nota final
PT=float(input("Ingresa tu nota de Tareas: "))
PI=float(input("Ingresa tu nota de Interrogaciones: "))
NE=float(input("Ingresa tu nota del Examen: "))
PP=float(input("Ingresa tu nota de la Presentación: "))

print(round((0.3*PT+0.3*PI+0.3*NE+0.1*PP),1))
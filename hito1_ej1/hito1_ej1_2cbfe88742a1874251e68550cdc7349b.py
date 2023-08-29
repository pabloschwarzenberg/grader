#Nota final

PT = float(input("Tareas: "))
PI = float(input("Interrograciones: "))
NE= float(input("Examen: "))
PP = float(input("Presentación: "))

PF = 0.3*PT+0.3*PI+0.3*NE+0.2*PP
print(round(PF,1))
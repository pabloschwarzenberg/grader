#Nota final
PT = float(input("Nota tareas: "))
PI = float(input("Nota interrogaciones: "))
NE = float(input("Nota examen: "))
PP = float(input("Nota presentación: "))
suma = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
notafinal = round(suma,1)
print("Su notal fnal es", notafinal)           


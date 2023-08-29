#Nota final
PT = float(input("Ingrese promedio trabajos: "))
PI = float(input("Ingrese promedio interrogaciones: "))
NE = float(input("Ingrese nota obtenida en examen: "))
PP = float(input("Ingrese promedio presentaciones: "))

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("El promedio final es", round (promedio,1))
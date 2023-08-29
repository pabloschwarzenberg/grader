#Nota final
PT = float(input("ingrese promedio de las tareas: "))
PI = float(input("Ingrese promedio de las interrogaciones: "))
NE = float(input("Ingrese promedio del examen: "))
PP = float(input("Ingrese promedio de la presentación: "))
promedio = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("El promedio de tus notas es:"  "{0:.1f}".format(promedio))     
#Nota final
PT = float(input("ingrese la nota de las tareas: "))
PI = float(input("Ingrese la nota de las interrogaciones: "))
NE = float(input("Ingrese la nota del examen: "))
PP = float(input("Ingrese la nota de la presentación: "))
promedio = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("El promedio de tus notas es:"  "{0:.1f}".format(promedio))

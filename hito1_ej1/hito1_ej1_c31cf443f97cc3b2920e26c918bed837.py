#Nota final
PT = float(input("Ingresar notas de Tareas:"))
PI = float(input("Ingresar notas de Interrogaciones:"))
NE = float(input("Ingresar nota de Examen:"))
PP = float(input("Ingresar nota de presentacion:"))

promedio = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print("El resultado de sus notas es:", "{:.1f}".format(promedio))      
#Nota final
PT = float(input("Introduzca la nota de sus tareas:"))
PI = float(input("Introduzca la nota de sus interrogaciones"))
NE = float(input("Introduzca la nota de su examen"))
PP = float(input("Introduzca la nota de su presentacion"))
# dar la ecuacion del promedio
promedio = ((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))
#imprimir el resultado
print("su promedio final es:", round(promedio, 1))
     
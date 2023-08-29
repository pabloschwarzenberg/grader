#Nota final
print("calcular el promedio final.")
PT = float(input("ingresa la nota de las Tareas: "))
PI = float(input("ingresa la nota de las Interrogaciones: "))
NE = float(input("ingresa la nota del Examen: "))
PP = float(input("ingresa la nota de la Presentación: "))

promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
promedio_redondeado = round(promedio, 1)

print("El promedio final es:", promedio_redondeado)



     
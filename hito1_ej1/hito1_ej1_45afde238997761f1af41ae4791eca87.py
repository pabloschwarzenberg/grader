
PT = float(input("Ingrese la nota de Tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota de Examen: "))
PP = float(input("Ingrese la nota de Presentacion: "))


promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP


promedio_redondeado = round(promedio, 1)


print("El promedio final es:", promedio_redondeado)


      
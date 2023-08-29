#Nota final
 def calcular_promedio_final(PT, PI, NE, PP):
    promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    promedio_redondeado = round(promedio, 1)
    print("El promedio final es:", promedio_redondeado)

PT = float(input("Ingrese la nota de las Tareas (0-100): "))
PI = float(input("Ingrese la nota de las Interrogaciones (0-100): "))
NE = float(input("Ingrese la nota del Examen (0-100): "))
PP = float(input("Ingrese la nota de la Presentación (0-100): "))

calcular_promedio_final(PT, PI, NE, PP)     
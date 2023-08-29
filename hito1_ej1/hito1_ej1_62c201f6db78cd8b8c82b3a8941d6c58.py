try:
    PT = float(input("Ingresa la nota de Tareas: "))
    PI = float(input("Ingresa la nota de Interrogaciones: "))
    NE = float(input("Ingresa la nota de Examen: "))
    PP = float(input("Ingresa la nota de Presentación: "))

    promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    promedio_final = round(promedio_final, 1)

    print("El promedio final es:", promedio_final)

except ValueError:
    print("Debes ingresar números válidos para las notas.")


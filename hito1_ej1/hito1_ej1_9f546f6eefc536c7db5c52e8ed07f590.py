def calcular_promedio_final():
    try:
        tareas = float(input("Ingresa la nota de Tareas (PT): "))
        interrogaciones = float(input("Ingresa la nota de Interrogaciones (PI): "))
        examen = float(input("Ingresa la nota de Examen (NE): "))
        presentacion = float(input("Ingresa la nota de Presentación (PP): "))

        promedio_final = 0.3 * tareas + 0.3 * interrogaciones + 0.3 * examen + 0.1 * presentacion
        promedio_final_aproximado = round(promedio_final, 1)

        print("El promedio final es: {:.1f}".format(promedio_final_aproximado))
    except ValueError:
        print("Error: Ingresa solo valores numéricos.")

calcular_promedio_final()




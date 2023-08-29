def calcular_promedio_final():
    # Solicitar al usuario las cuatro notas
    pt = float(input("Ingresa la nota de las Tareas (PT): "))
    pi = float(input("Ingresa la nota de las Interrogaciones (PI): "))
    ne = float(input("Ingresa la nota del Examen (NE): "))
    pp = float(input("Ingresa la nota de la Presentación (PP): "))

    # Calcular el promedio final
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp

    # Imprimir el resultado redondeado a un decimal
    print("El promedio final es:", round(promedio_final, 1))


# Llamar a la función para calcular el promedio final
calcular_promedio_final()

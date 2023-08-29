def calcular_promedio_final():
    """
    Función para calcular el promedio final de un estudiante.
    Se solicitarán las notas de PT, PI, NE y PP al usuario, y se calculará el promedio final
    utilizando la fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP.

    Retorna:
    - promedio_final: promedio final redondeado a un decimal
    """
    # Solicitar las notas al usuario
    pt = float(input("Ingrese la nota de Tareas (PT): "))
    pi = float(input("Ingrese la nota de Interrogaciones (PI): "))
    ne = float(input("Ingrese la nota de Examen (NE): "))
    pp = float(input("Ingrese la nota de Presentacion (PP): "))

    # Calcular el promedio final
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp

    # Redondear el resultado a un decimal
    promedio_final = round(promedio_final, 1)

    return promedio_final

# Calcular el promedio final y mostrar el resultado
promedio = calcular_promedio_final()
print("El promedio final es:", promedio)

      
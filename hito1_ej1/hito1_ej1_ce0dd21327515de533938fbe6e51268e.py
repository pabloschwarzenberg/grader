def calcular_promedio_final():
    # Solicitar las cuatro notas al usuario
    pt = float(input("Ingresa la nota de Tareas: "))
    pi = float(input("Ingresa la nota de Interrogaciones: "))
    ne = float(input("Ingresa la nota de Examen: "))
    pp = float(input("Ingresa la nota de Presentacion: "))

    # Calcular el promedio final
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp

    # Imprimir el resultado redondeado a un decimal
    print("El promedio final es:", round(promedio_final, 1))

# Llamar a la función para ejecutar el programa
calcular_promedio_final()

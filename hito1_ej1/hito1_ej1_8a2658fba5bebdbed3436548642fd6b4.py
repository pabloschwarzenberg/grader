def calcular_promedio_final():
    pt = float(input("Ingrese la nota de Tareas (PT): "))
    pi = float(input("Ingrese la nota de Interrogaciones (PI): "))
    ne = float(input("Ingrese la nota de Examen (NE): "))
    pp = float(input("Ingrese la nota de Presentacion (PP): "))

    #Calcular el promedio con la siguiente variable
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp

    #Dar el promedio y que sea redondeado a un decimal

    print("El promedio final es:", round(promedio_final, 1))

calcular_promedio_final()

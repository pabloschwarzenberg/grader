#Nota final

#Transformación
while True:

    PT = float(input("Ingrese la nota de Tareas:  "))
    PI = float(input("Ingrese la nota de Interrogaciones:  "))
    NE = float(input("Ingrese la nota de Examen:  "))
    PP = float(input("Ingrese la nota de Presentación:  "))
    if PT >= 1.0 and PT <= 7.0 and NE >= 1.0 and NE <= 7.0 and PP >= 1.0 and PP <= 7.0:
        Promedio_final = round(0.3 * PT + 0.3 *PI + 0.3 * NE + 0.1 * PP,1)
        print("Su promedio final es" , Promedio_final)
        break
    else:
        print("Una de las notas ingresadas no es valida ")      
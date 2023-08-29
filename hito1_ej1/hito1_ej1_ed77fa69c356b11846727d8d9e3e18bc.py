#Nota final
PT = float(input("Ingrese su promedio de tareas:"))
PI = float(input("Ingrese su promedio de interrogaciones:"))
NE = float(input("Ingrese su nota de examen:"))
PP = float(input("Ingrese su nota de presentacion:"))
if 7 >= PT >= 1:
    if 7 >= PI >= 1:
        if 7 >= NE >= 1:
            if 7 >= PP >=1:
                NF = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
                print("Su nota final es:", NF)

            else:
                print("Su nota de presentación no fue agregado correctamente")

        else:
            print("Su nota de examen no fue agregado correctamente")

    else:
        print("Su nota de promedio de interrogaciones no fue agregado correctamente")

else:
    print("Su nota de promedio de tareas no fue agregado correctamente")
      
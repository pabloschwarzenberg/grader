#Nota final
#ENTRADA

PT = float(input("Ingrese la nota de su tarea: "))
PI = float(input("Ingrese la nota de la interrogacion: "))
NE = float(input("Ingrese la nota de el examen: "))
PP = float(input("Ingrese la nota de la presentacion: "))

#PROCESO

promedio = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
redondear = round(promedio, 1)

#SALIDA

print("La nota final es: {}".format(redondear))

    
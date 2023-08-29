#Nota final
PT = float(input("Ingrese la nota de las tareas: "))
PI = float(input("Ingrese la nota de las interrogaciones: "))
NE = float(input("Ingrese la nota del exámen: "))
PP = float(input("Ingrese la nota de la presentación: "))

promedio = (0.3*PT+ 0.3*PI + 0.3*NE + 0.1*PP)

print("el promedio final es:", round(promedio,1))
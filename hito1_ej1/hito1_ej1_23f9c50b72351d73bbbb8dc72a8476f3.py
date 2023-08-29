#Nota final

PT = eval(input("Ingrese la nota de Tareas: "))
PI = eval(input("Ingrese la nota de Interrogaciones: "))
NE = eval(input("Ingrese la nota del Exámen: "))
PP = eval(input("Ingrese la nota de su Presentación: "))

Promedio = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)

print("La nota del promedio final es: ",round(Promedio,1),)


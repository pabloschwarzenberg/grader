#Nota final
PT = float(input("Ingresar la nota de las Tareas: "))
PI = float(input("Ingresar la nota de las Interrogaciones: "))
NE = float(input("Ingresar la nota de el Examen: "))
PP = float(input("Ingresar la nota de la Presentación: "))

p = round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP, 2)
print("el promedio final es: ", p)
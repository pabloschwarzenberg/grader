#Nota final
PT = float(input("Ingrese su promedio de notas de tareas: "))
PI = float(input("Ingrese su promedio de notas de Interrogaciones: "))
NE = float(input("Ingrese su nota de examen: "))
PP = float(input("Ingrese su nota de presentación: "))
print("Su nota final es: ", (round(0.3*(PT + NE + PI) + 0.1 * PP, 1)))
#Nota final

PT = float(input("Ingresa la nota de tus tareas: "))
PI = float(input("Ingresa la nota de tus interrogaciones: "))
NE = float(input("Ingresa tu nota del examen: "))
PP = float(input("Ingresa tu nota de la presentación: "))

promedio = round(0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP, 1)

print("Tu promedio es " + str(promedio))
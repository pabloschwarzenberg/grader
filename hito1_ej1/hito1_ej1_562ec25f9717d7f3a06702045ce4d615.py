#Nota final
PT = float(input("Ingrese el promedio de notas de sus tareas: "))
PI = float(input("Ingrese el promedio de notas de interrogaciones: "))
NE = float(input("Ingrese su nota de exámen: "))
PP = float(input("Ingrese el promedio de presentación: "))

promedio = (0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)

print("Su promedio final es: ", round (promedio,1))

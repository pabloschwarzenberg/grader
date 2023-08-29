PT = float(input("escriba su nota de tareas: "))
PI = float(input("escriba su nota de interrogaciones: "))
NE = float(input("escriba su nota de examen: "))
PP = float(input("escriba su nota de presentacion: "))

promedio = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
print("su promedio final es: ", promedio)
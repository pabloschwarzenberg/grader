#Nota final
# Entrada

PT = float(input("Ingrese su nota de tareas: "))
PI = float(input("Ingrese su nota de interrogaciones: "))
NE = float(input("Ingrese su nota de examen: "))
PP = float(input("Ingrese su nota de presentaciones: "))

# Procesamiento

promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Salida

print("Su promedio es: " , round(promedio, 1))
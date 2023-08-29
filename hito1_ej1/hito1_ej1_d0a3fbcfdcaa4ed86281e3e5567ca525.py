# Ingreso de notas
PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de interrogaciones: "))
NE = float(input("Ingrese la nota de examen: "))
PP = float(input("Ingrese la nota de presentaciones: "))

# Calculo de promedio
promedio = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)

# Final
print("El promedio es: ",promedio)
      
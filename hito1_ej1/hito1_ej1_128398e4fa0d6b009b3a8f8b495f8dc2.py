#Nota final
# Entradas

PT = float(input("Ingrese la nota de las tareas: "))
PI = float(input("Ingrese la nota de las interrogaciones: "))
NE = float(input("Ingrese la nota del examen: "))
PP = float(input("Ingrese la nota de la presentacion: "))

# Proceso para el promedio

promedio = round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP,1)

# Salida

print("El promedio es de", promedio)      
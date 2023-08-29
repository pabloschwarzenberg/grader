#Nota final
PT = float(input("Ingresa la nota de tus tareas: "))
PI = float(input("Ingresa la nota de las interrogaciones: "))
NE = float(input("Ingresa nota del exámen: "))
PP = float(input("Ingresa nota de presentacion: "))
promedio = ((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))
promedio = round(promedio,1)

print("El promedio de las notas es ",promedio)
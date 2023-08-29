PT = float(input("ingrese nota de tareas: "))
PI = float(input("ingrese nota de interrogaciones: "))
NE = float(input("ingrese nota de examen: "))
PP = float(input("ingrese nota de presentacion: "))

calculo = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print(round(calculo, 1))

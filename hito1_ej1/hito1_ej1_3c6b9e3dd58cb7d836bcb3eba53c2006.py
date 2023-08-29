#Nota final
PT = float(input("ingresa promedio de notas de los trabajos: "))
PI = float(input("ingresa promedio de notas de las interrogaciones: "))
NE = float(input("ingresa nota de examen: "))
PP = float(input("ingresa promedio de presentaciones: "))

promedio = (0.3*PT+0.3*PI+0.3*NE+0.1*PP)

print("promedio finales es", round(promedio,1))
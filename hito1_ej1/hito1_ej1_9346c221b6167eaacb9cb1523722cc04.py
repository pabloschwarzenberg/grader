#Nota final
PT = float(input("Ingresa promedio de notas de tus trabajos: "))
PI = float(input("Ingresa promedio de notas de tus interrogaciones: "))
NE = float(input("ingresa nota de examen: "))
PP = float(input("ingresa promedio de presentaciones: "))

promedio = (0.3*PT+0.3*PI+0.3*NE+0.1*PP)

print("tu promedio final es", round(promedio,1))
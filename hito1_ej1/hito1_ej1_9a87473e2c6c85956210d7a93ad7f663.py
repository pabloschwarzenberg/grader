#Nota final

PT = eval(input("Ingrese el promedio de tareas: "))
PI = eval(input("Ingrese el promedio de interrogaciones: "))
NE = eval(input("Ingrese el promedio de examen: "))
PP = eval(input("Ingrese el promedio de presentación: "))

promedio = round((0.3 * PT) + (0.3*PI) + (0.3*NE) + (0.1*PP), 2)
print(promedio)
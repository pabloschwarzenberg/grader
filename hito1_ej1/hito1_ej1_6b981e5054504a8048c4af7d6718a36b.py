#Nota final
PT = eval(input("Ingrese la nota de tareas: "))
PI = eval(input("Ingrese la nota de interrogaciones: "))
NE = eval(input("Ingrese la nota de examen: "))
PP = eval(input("Ingrese la nota de presentaciones: "))

promedio = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print(round(promedio, 1))

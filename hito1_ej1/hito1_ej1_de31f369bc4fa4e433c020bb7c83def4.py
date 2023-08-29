#entrada.

PT = float(input("escriba aqui la nota de las Tareas: "))
PI = float(input("escriba aqui la nota de las Interrogaciones: "))
NE= float(input("escriba aqui la nota del examen: "))
PP = float(input("escriba aqui la nota de la Presentacion: "))

#operaciones.

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
promediof = round(promedio, 2)
print(promediof)
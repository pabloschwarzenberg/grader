#Nota final
PT = float(input("ingrese nota tarea: "))
PI = float(input("ingrese nota interrogaciones: "))
NE = float(input("ingrese nota examen: "))
PP = float(input("ingrese nota presentaciones: "))
promedio = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
Promediored = round(promedio, 1)
print(Promediored)
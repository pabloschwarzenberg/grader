#Nota final
PT = float(input("Nota de tareas: "))
PI = float(input("Nota de interrogaciones: "))
NE = float(input("Nota de Examen: "))
PP = float(input("Nota de presentacion: "))

#Proceso
i = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
x = round(i, 1)
print(x)      
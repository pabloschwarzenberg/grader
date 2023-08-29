#Nota final
PT = float(input("Ingrese nota de tareas: "))
PI = float(input("Ingrese nota de interrogaciones: "))
NE = float(input("Ingrese nota de examen: "))
PP = float(input("Ingrese nota de presentacion: "))
promedio = (0.3*PT+0.3*PI+0.3*NE+0.1*PP)
if(promedio%0.1 >= 0.5) : promedio + 0.1
promedio = promedio - promedio%0.1
print(promedio)
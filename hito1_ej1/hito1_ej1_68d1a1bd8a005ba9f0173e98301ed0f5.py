#Nota final
PT = eval(input("ingrese nota de tareas: "))
PI = eval(input("ingrese nota de interrogaciones: "))
NE = eval(input("ingresen nota de examen: "))
PP = eval(input("ingrese nota de presentacion: "))
promedio = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print("el promedio de las cuatro notas es:", round(promedio,1))  
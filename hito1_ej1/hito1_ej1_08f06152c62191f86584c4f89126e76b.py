#Nota final
PT = float(input("Ingresar nota de tareas: "))
PI = float(input("Ingresar nota de interrogaciones: "))
NE= float(input("Ingresar nota de examen: "))
PP= float(input("Ingresar nota de presentacion: "))

v=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)

v2= round(v,1)

print("El promedio de las notas es: ",v2)
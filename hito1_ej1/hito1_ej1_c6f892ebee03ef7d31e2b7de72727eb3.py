PT = float(input("ingresar nota de tareas"))
PI = float(input("ingresar nota de interrogaciones"))
NE= float(input("ingresar nota de examen"))
PP= float(input("ingresar nota de presentacion"))

v=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)

v2= round(v,1)

print("el promedio de las notas es:",v2)
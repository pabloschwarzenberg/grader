print("ingresar nota de tareas: ")
PT = (float(input("Nota de tareas")))
print("ingresar nota de las interrogaciones: ")
PI = (float(input("nota de interrogaciónes")))
print("ingresar notas del examen: ")
NE = (float(input("nota de examen")))
print("ingresar nota de presentación: ")
PP = (float(input("nota de presentación")))
p = 0.3*PT+0.3*PI+0.3*NE+0.1*PP
print("promedio final: ",round(p,1))
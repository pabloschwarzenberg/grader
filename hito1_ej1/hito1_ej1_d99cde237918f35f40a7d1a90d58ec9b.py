#Nota final
PT=float(input("Ingrese nota de tareas"))
PI=float(input("Ingrese nota de interrogaciones"))
NE=float(input("Ingrese la nota de examen"))
PP=float(input("ingrese la nota de presentacion"))
pr= (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print("el promedio final es", round(pr,1))
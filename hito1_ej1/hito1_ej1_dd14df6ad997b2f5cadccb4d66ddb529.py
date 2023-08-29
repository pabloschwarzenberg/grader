#Nota final
PT=float(input("Ingrese nota de tareas"))
PI=float(input("Ingrese nota de interrogaciones"))
NE=float(input("Ingrese nota Examen"))
PP=float(input("Ingrese la nota de presentación"))
PR= (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print("el promedio final es:", round(PR,1))
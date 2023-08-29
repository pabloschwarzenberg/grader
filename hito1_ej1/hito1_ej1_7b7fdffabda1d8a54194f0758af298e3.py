#Nota final
PT= float(input("Ingrese nota de tareas: "))
PI= float(input("Ingrese nota de interrogaciones: "))
NE= float(input("Ingrese nota de Examen: "))
PP= float(input("Ingrese nota de Presentacion: "))
PF= 0.3*PT+0.3*PI+0.3*NE+0.1*PP
PF_2= round(PF,1)
print("el promedio final es: ",PF_2)
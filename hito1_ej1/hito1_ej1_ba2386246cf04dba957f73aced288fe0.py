#Nota final
T=float(input("ingrese nota de tareas: "))
I=float(input("ingrese nota de interrogacion:"))
E=float(input("ingrese nota de examen:"))
P=float(input("ingree nota de presentacion:"))

promedio_final=T*0.3+I*0.3+E*0.3+0.1*P

print(round(promedio_final, 1))
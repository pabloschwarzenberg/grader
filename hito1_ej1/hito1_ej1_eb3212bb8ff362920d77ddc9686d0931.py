#Nota final
PT=float(input("Ingrese nota de tareas:"))
PI=float(input("Ingrese nota de Interrogaciones:"))
NE=float(input("Ingrese nota de examen:"))
PP=float(input("Ingrese nota de Presentacion:"))
Promedio=PT*0.3+PI*0.3+NE*0.3+PP*0.1 
Promedio_redondeado=round(Promedio,1)
print("El promedio final es:", Promedio_redondeado)
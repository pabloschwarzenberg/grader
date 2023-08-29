#Nota final
PT= float(input("ingrese la nota de tareas: "))
PI= float(input("ingrese la nota de interrogaciones: "))
NE= float(input("ingrese la nota de examen: "))
PP= float(input("ingrese la nota de presentacion: "))

PF= round((PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1),1)
print("el promedio final es:", PF)      
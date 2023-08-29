#Nota final
#Creado por Kenzo Valdebenito
PT= float(input("Ingrese la nota de la tarea "))
PI= float(input("Ingrese la nota de las interrogaciones "))
NE= float(input("Ingrese la nota del examen "))
PP= float(input("Ingrese la nota de la presentacion "))
PF= round((PT*0.3 + PI*0.3 + NE*0.3 + PP*0.1),1)
print("el promedio final de las notas es", PF)
#Nota final
PT=float(input("ingrese la nota de Tareas:"))
PI=float(input("ingrese la nota de interrogaciones:"))
NE=float(input("ingrese la nota de examen:"))
PP=float(input("ingrese la nota de presentacion:"))
#Procesamiento
NF= 0.3*PT+0.3*PI+0.3*NE+0.1*PP
#Salida
print("el resultado redondeado con un decimal es:", round(NF,1))

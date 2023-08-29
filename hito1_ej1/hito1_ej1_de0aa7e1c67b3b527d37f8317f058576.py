#Nota final
print("ingresa la nota de la tarea: ")
PT = (float(input("nota de la tarea: ")))
print("ingresa la nota de la interrogaciones: ")
PI=(float(input("nota de las interrogaciones: ")))
print("ingresa la nota del examen: ")
NE=(float(input("nota del examen: ")))
print("ingresa la nota del presentacion: ")
PP=(float(input("nota de la presentacion: ")))
#proceso
P=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
#salida
print("el promedio de la 4 notas: ",round(P,1))
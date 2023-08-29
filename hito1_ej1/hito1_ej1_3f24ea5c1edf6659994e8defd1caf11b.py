#Nota final
#Entrada

PT=float(input("Ingrese la nota de sus tareas: "))
PI=float(input("Ingrese la nota de sus interrogaciones: "))
NE=float(input("Ingrese la nota de su examen: "))
PP=float(input("Ingrese la nota de su presentacion: "))

#Formula
PF = (0.3*PT+0.3*PI+0.3*NE+0.1*PP)

#Resultado
print("Su promedio final es: ",PF)     
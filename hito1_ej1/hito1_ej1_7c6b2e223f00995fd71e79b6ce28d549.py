#Nota final
print("Ingrese las siguientes calificaciones")
PT=float(input("Promedio Tareas:"))
PI=float(input("Promedio Interrogaciones:"))
NE=float(input("Nota Examen:"))
PP=float(input("Promedio Presentaciones:"))
print("Su promedio final es:", round(0.3*PT+0.3*PI+0.3*NE+0.1*PP,1))
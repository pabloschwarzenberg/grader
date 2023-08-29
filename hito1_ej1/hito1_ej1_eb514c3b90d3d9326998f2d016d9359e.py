#Nota final
PT = float(input("Ingrese la nota final de tareas:"))
PI = float(input("Ingrese la nota final de las interrogaciones:"))
NE = float(input("Ingrese la nota final del examen:"))
PP = float(input("Ingrese la nota final de la presentacion:"))
pr = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print("El promedio final es ", round(pr,1))
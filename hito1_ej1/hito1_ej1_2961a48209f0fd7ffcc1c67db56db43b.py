#Nota final
PT=float(input("Ingrese nota Tareas:"))
PI=float(input("Ingrese nota Interrogantes:"))
NE=float(input("Ingrese nota Examen:"))
PP=float(input("Ingrese nota Presentacion:"))
total= (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("El promedio final es:",(round(total,1)))      
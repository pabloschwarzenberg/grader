#Nota final
PT = float(input("Ingrese nota Tareas: "))
PI = float(input("Ingrese nota Interrogaciones: "))
NE = float(input("Ingrese nota Examen: "))
PP = float(input("Ingrese nota Presentaciones : "))
promedio_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("El promedio Final del curso es: ",round(promedio_final,1))
#Nota final
PT = float(input("ingrese nota de tareas:"))
PI = float(input("ingrese nota de interrogaciones:"))
NE = float(input("ingrese nota de examen:"))
PP = float(input("ingrese nota de presentacion:"))

promedio = float(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
promedio_final= round(promedio,1)
print("el promedio final es:",str(promedio_final))
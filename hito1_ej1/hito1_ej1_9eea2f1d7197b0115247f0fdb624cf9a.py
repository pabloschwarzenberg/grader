#Nota final
print("Calculo de Nota Final")
PT= float(input("Ingrese nota de Tareas: "))
PI= float(input("Ingrese nota de Interrogaciones: "))
NE= float(input("Ingrese nota de Examen: "))
PP= float(input("Ingrese nota de Presentacion: "))

NF= 0.3*PT+0.3*PI+0.3*NE+0.1*PP

print("Su Nota Final es:", round(NF, 1))
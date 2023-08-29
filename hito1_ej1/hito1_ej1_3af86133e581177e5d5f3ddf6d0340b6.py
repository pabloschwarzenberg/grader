#Nota final
PT=float(input("Ingrese nota de Tareas: "))
PI=float(input("Ingrese nota de Interrogaciones: "))
PE=float(input("Ingrese nota de Exámen: "))
PP=float(input("Ingrese nota de Presentación: "))
calculo= round((PT*0.3)+(PI*0.3)+(PE*0.3)+(PP*0.1),1)
print("El promedio es:", calculo)
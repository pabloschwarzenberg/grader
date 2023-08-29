#Nota final
print()
print("Promedio Final".center(50))
PT=float(input("Ingresa tu nota de Tareas: "))
PI=float(input("Ingresa tu nota de Interrogaciones: "))
NE=float(input("Ingresa tu nota de Examen: "))
PP=float(input("Ingresa tu nota de Presentacion: "))
pr_final=round((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP),1)
print("Tu promedio final es",pr_final)
     
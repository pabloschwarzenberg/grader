#Nota final
PT=float(input("Ingrese nota de tus tareas: "))
PI=float(input("Ingrese nota de tus interrogaciones: "))
NE=float(input("Ingrese nota de EXAMEN: "))
PP=float(input("Ingrese nota de PRESENTACION: "))

notafinal=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print(round(notafinal,1))
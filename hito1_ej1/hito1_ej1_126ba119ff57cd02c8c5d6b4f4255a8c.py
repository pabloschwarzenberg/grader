#Nota final
PT=float(input("Ingrese Nota de tareas: "))
PI=float(input("Ingrese Nota de interrogaciones: "))
NE=float(input("Ingrese Nota de examen: "))
PP=float(input("Ingrese Nota de presentacion: "))
resultado=round((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP),1)
print(resultado)
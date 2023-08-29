#Nota final
print("Bienvenido, por favor indiquenos sus notas")
PT=float(input("Porcentaje nota tareas: "))
PI=float(input("Porcentaje nota interrogaciones: "))
NE=float(input("Nota examen: "))
PP=float(input("Nota presentacion: "))
NF=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print("Su nota final es:",NF)
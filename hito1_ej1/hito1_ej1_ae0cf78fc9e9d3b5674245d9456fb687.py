#Nota final
PT=float(input("ingrese su promedio de tareas: "))
PI=float(input("ingrese su promedio de interrogaciones: "))
NE=float(input("ingrese su nota de examen: "))
PP=float(input("ingrese su promedio de presentacion: "))

NF=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print("su nota final es", NF)
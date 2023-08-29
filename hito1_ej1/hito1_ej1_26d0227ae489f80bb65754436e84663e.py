#Nota final
PT=eval(input("Ingrese su nota de tareas: "))
PI=eval(input("Ingrese su nota de interrogaciones: "))
NE=eval(input("Ingrese su nota de examen: "))
PP=eval(input("Ingrese su nota de presentacion: "))
PF=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print(round(PF, 1))
#Nota final
PT=float(input("ingrese nota de tareas: "))
PI=float(input("ingrese nota de interrogaciones: "))
NE=float(input("ingrese nota de examenes: "))
PP=float(input("ingrese nota de presentación: "))
Notafinal=0.3*PT+0.3*PI+0.3*NE+0.1*PP
Notaredondeada=round(Notafinal, 1)
print(Notaredondeada)
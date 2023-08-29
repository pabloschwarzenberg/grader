#Nota final
PT=float(input("Ingrese nota de Tareas: "))
PI=float(input("Ingrese nota de Interrogaciones: "))
NE=float(input("Ingrese nota de Examen"))
PP=float(input("Ingrese nota de Presentación"))

PF=(0.3*PT+0.3*PI+0.3*NE+0.1*PP)//0.1
print((PF/10))

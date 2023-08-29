#Nota final
PT=float(input("ingrese nota de tareas: "))
PI=float(input("ingrese nota de interrogaciones:"))
NE=float(input("ingrese nota de examen: "))
PP=float(input("ingrese nota de presentacion: "))

PF=((PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1))
PF_redondeado=round(PF, 1)

print("Tu promedio final es:")
print(PF_redondeado)
#Nota final
PT=float(input("Ingrese nota de tareas: "))
PI=float(input("Ingrese nota de interrogaciones: "))
NE=float(input("Ingrese nota de examen: "))
PP=float(input("Ingrese nota de presentacion: "))
NF=((float(0.3)*PT)+(float(0.3)*PI)+(float(0.3)*NE)+(float(0.1)*PP))
print(str(round(NF,1)))
      
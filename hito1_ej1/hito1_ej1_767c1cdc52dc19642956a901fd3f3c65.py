#Nota final
PT=input("nota de tareas: ")
PT=float(PT)
PI=input("nota de interrogaciones: ")
PI=float(PI)
NE=input("nota de examen: ")
NE=float(NE)
PP=input("nota de presentación: ")
PP=float(PP)
nota= 0.3*PT+0.3*PI+0.3*NE+0.1*PP
nota_aprox=round(nota,1)
print(nota_aprox)


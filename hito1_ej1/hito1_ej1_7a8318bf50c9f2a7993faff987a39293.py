#Nota final
PT=float(input("Ingrese nota de tareas: "))
PI=float(input("Ingrese nota de interrogaciones: "))
NE=float(input("Ingrese nota del exámen: "))
PP=float(input("Ingrese nota de la presentación: "))
nota=0.3*PT+0.3*PI+0.3*NE+0.1*PP
final=round(nota,1)
print("Su nota final del curso es",final)
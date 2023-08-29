
PT=float(input("Nota tareas: "))
PI=float(input("Nota interrogaciones: "))
NE=float(input("Nota examen: "))
PP=float(input("Nota presentación: "))
NF=round(0.3*PT+0.3*PI+0.3*NE+0.1*PP,1)

print("Tu nota final es",NF)
     
#Nota final
PT=float(input("Inserte nota tareas:"))
PI=float(input("Inserte nota interrogaciones:"))
NE=float(input("Inserte nota examen:"))
PP=float(input("Inserte notas presentación:"))
Notafinal=round((0.3*PT+0.3*PI+0.3*NE+0.1*PP),1)
print("Tu nota final es:", Notafinal)

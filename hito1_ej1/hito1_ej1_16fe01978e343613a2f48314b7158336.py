#Nota final
PP = float(input("Deme su nota de presentación:"))
PT = float(input("Deme su nota de tareas:"))
PI = float(input("Deme su nota de interrogaciones:"))
NE = float(input("Deme su nota del examen:"))
NF = 0.3*PT+0.3*PI+0.3*NE+0.1*PP
print("Su nota final es:",NF)
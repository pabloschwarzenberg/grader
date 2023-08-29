#Nota final
PT=float(input("Ingrese el puntaje de sus tareas: "))
PI=float(input("Ingrese el puntaje de sus interrogaciones: "))
NE=float(input("Ingrese el puntaje de sus exámenes: "))
PP=float(input("Ingrese el puntaje de su presentación: "))
PF= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("La nota final es",round(PF,1))
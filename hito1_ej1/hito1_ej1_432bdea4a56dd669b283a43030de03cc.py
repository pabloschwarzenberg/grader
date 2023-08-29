#Nota final
PT=float(input("Introduzca la nota de tareas: "))
PI=float(input("Introduzca la nota de Interrogaciones: "))
NE=float(input("Ingrese la nota de Examen: "))
PP=float(input("Ingrese nota de Pesentación: "))
NF=round(0.3*PT+0.3*PI+0.3*NE+0.1*PP ,1) 
print("La nota final es: ", NF)     
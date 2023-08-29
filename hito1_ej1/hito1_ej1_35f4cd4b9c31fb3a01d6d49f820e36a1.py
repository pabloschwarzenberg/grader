#Nota final
PT = float(input("ingrese nota tareas: ")) 
PI = float(input("ingrese nota interrogaciones: "))
NE = float(input("ingrese nota examen: "))
PP = float(input("ingrese nota presentacion: "))
n_f= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("la nota final del curso es: ", round(n_f,1))
#Nota final
PT = float(input("ingrese nota tareas: "))
PI = float(input("ingrese nota interrogacionses: "))
NE = float(input("ingrese nota examen: "))
PP = float(input("ingrese nota presentacion: "))
promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
promedioR=round(promedio,1)
print(promedioR)
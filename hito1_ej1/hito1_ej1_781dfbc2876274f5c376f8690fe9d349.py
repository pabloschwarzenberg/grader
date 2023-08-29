#Nota final
print("por favor, ingrese 4 notas: ")
PT=float(input("ingrese nota tareas: "))
PI=float(input("ingrse nota interrogaciones:"))
NE=float(input("ingrese nota examen: "))
PP=float(input("ingrese nota presentacion: "))

x = 0.3*PT+0.3*PI+0.3*NE+0.1*PP

print("el promedio es:", (round(x, 1)))
      
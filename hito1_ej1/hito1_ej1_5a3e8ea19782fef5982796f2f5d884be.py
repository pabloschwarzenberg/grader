#Nota final
PT=float(input("Ingrese nota de tareas "))
PI=float(input("Ingrese nota interrogaciones "))
NE=float(input("Ingrese nota exámen "))
PP=float(input("Ingrese nota presentación "))
promedio= (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("su nota final es ", round(promedio,1))      
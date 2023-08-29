#Nota final
PT=float(input("nota tareas:"))
PI=float(input("nota interrogaciones:"))
NE=float(input("nota examen:"))
PP=float(input("nota presentacion:"))
promedio=float(0.3*PT+0.3*PI+0.3*NE+0.1*PP)
promedio=round(promedio,1)
print(promedio)

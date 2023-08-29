#Nota final
PT=float(input("Nota tareas:"))
PI=float(input("Nota interogaciones:"))
NE=float(input("Nota examen:"))
PP=float(input("Nota presentacion:"))

suma=(0.3*PT) + (0.3*PI) +(0.3*NE) + (0.1*PP)
print("nota final: ",round(suma,1))
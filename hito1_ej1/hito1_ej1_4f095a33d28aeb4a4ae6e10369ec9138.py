#Nota final
PT=float(input("promedio tareas? "))
PI=float(input("promedio interrogaciones? "))
NE=float(input("nota examen? "))
PP=float(input("nota presentacion? "))
(nota_final)=float(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("Tu promedio final es:", round(nota_final,1))

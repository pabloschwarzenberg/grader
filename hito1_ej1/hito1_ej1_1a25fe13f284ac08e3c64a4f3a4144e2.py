#Nota final
PT=float(input("ingresa la nota de tareas:"))
PI=float(input("ingresa la nota de interrogaciones:"))
NE=float(input("ingresa la nota de examen:"))
PP=float(input("ingresa la nota de presentacion:"))
promedio=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
round(promedio,2)
print(promedio)
#Nota final
PT=float(input("ingresa la nota de tareas: "))
PI=float(input("ingresa la nota de interroganciones: "))
NE=float(input("ingresa la nota de examen: "))
PP=float(input("ingresa la nota de presentacion:"))
pf=round((0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP),1)
print("el promedio final es",pf)      
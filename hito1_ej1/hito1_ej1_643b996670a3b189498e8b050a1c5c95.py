PT=float(input("ingrese el promedio tareas"))
PI=float(input("ingrese el promedio interrogaciones"))
NE=float(input("ingrese nota examen"))
PP=float(input("ingrese nota presentacion"))
x=0.1
y=0.3
notafinal = y*PT+y*PI+y*NE+x*PP
promediofinal=round(notafinal,1)
print("La nota final es:",promediofinal)
PT=int(input("ingrese nota de tareas"))
PI=int(input("ingrese nota de interrogaciones"))
NE=int(input("ingrese nota de examen"))
PP=int(input("ingrese nota de presentacion"))

promedio= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("su resultado es",round (promedio,1))
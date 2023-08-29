PT=float(input("ingrese nota de tareas"))
PI=float(input("ingrese nota de interrogaciones"))
NE=float(input("ingrese nota de examen"))
PP=float(input("ingrese nota de presentación"))
PT1= 0.3*PT
PI1= 0.3*PI
NE1=0.3*NE
PP1=0.1*PP
Promedio= PT1+PI1+NE1+PP1
print("el promedio de las notas es",round (Promedio,1))
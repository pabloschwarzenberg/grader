#Nota final
PT=float(input("Escribe tu nota de tareas"))
PI=float(input("Escribe tu nota de interrogaciones"))
NE=float(input("Escribe tu nota de examen"))
PP=float(input("Escribe tu nota de presentacion"))

promedio=((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP))
promedio=float(promedio)

if promedio >=4:
   print("Aprobaste tu curso con nota",round(promedio,1))
   
elif promedio <4:
   print("Reprobaste el curso con nota",round(promedio,1))
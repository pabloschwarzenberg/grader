PT=float(input("Ingrese el promedio de tareas:"))
PI=float(input("Ingrese el promedio de interrogaciones:"))
NE=float(input("Ingrese la nota de sue examen:"))
NP=float(input("Ingrese nota de presentación:"))

PF= PT*0.3 + PI*0.3 + NE*0.3 + NP*0.1
print("El promedio final es:", round((PF),1))



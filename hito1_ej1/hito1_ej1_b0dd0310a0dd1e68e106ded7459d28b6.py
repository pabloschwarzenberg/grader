#Nota final
PT=float((input("ingrese nota de tareas: ")))
PI=float((input("ingrese nota de interrogaciones: ")))
NE=float((input("ingrese nota de examen: ")))
PP=float((input("ingrese nota de presentación: ")))
pPT=(0.3*(PT))
pPI=(0.3*(PI))
pNE=(0.3*(NE))
pPP=(0.1*(PP))
promedio=(pPT+pPI+pNE+pPP)
from math import floor
print(round(promedio,1))      
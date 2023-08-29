#Nota final
from os import system
system ("cls")
PT=0 #tareas
PI=0 #Interrogaciones
NE=0 #Examen
PP=0 #Presentacion

#0.3PT + 0.3PI + 0.3NE + 0.1PP

PT= float(input("Ingrese nota de tareas: "))
PI= float(input("Ingrese nota de interrogaciones: "))
NE= float(input("Ingrese nota de examen: "))
PP= float(input("Ingrese nota de presentacion: "))

Prom= (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print(Prom)  
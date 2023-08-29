PT=float(input("Introdusca promedio tareas: "))
PI=float(input("Introdusca promedio interrogaciones: "))
NE=float(input("Introdusca nota examen: "))
PP=float(input("Introdusca nota presentación: "))

f=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
pf=round(f,1)
print("Promedio final del curso:",pf)      
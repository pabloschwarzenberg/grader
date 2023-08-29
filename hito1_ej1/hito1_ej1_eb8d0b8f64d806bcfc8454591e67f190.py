#Nota final
print("¿Cuáles son tus promedios de notas en Tareas(PT), Interrogaciones(PI), Examen (NE) y Presentación (PP)?")
PT=float(input("PT:"))
PI=float(input("PI:"))
NE=float(input("NE:"))
PP=float(input("PP:"))
print("Entonces, tu promedio de notas final de PT, PI, NE Y PP es")
Pf=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print("promedio final:",round(Pf,1))
print("---- PROMEDIO GENERAL ----\n")

PT=float(input("Ingrese notas de Tareas: "))
PI=float(input("Ingrese notas de Interrogaciones: "))
NE=float(input("Ingrese nota del Examen: "))
PP=float(input("Ingrese nota Presentacion: "))

PF=((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP))
pf=round(PF,1)
print("\n\tEl promedio final de la persona es : ",pf)

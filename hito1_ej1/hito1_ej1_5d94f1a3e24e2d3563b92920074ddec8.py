#Nota final
PT=float(input("promedio tareas:"))
PI=float(input("interrogaciones:"))
NE=float(input("examen:"))
PP=float(input("presentacion:"))
r=0.3*PT+0.3*PI+0.3*NE+0.1*PP
if r%0.1>=0.05:

    R = r - r%0.1 + 0.1

else:
    R = r - r%0.1 
print("promedio final:",R)


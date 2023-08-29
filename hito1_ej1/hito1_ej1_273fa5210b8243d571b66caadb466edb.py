#Nota final
PT=float(input("Inserte su nota de Tareas: "))
PI=float(input("Inserte su nota de Interrogaciones: "))
NE=float(input("Inserte su nota de Examen: "))
PP=float(input("Inserte su nota de Presentación: "))

PF=float(0.3*PT+0.3*PI+0.3*NE+0.1*PP)
print("Su promedio final es",round(PF,1),".")

if(PF>=4):
    print("Felicitaciones!!")
else:
    print("...Uy...")
    
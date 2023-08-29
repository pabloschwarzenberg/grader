#Nota final
PT=float(input("Ingresa tu tarea: "))
PI=float(input("Ingresa tu Interrogacion: "))
NE=float(input("Ingresa tu examen: "))
PP=float(input("Ingresa tu presentacion: "))
NF=float(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("Tu nota final es",round(NF,1))
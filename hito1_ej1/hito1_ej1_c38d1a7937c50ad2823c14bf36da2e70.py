#Nota final
PT = float(input("Ingrese nota por tareas: "))
PI = float(input("Ingrese nota por interrogaciones: "))
NE = float(input("Ingrese nota por examenes: "))
PP = float(input("Ingrese nota por presentacion: "))
PF = ((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))
round (PF, 1)
print ("El promedio final es: ", PF)
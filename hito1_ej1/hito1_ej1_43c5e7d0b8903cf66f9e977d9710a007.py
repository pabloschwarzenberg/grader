#Nota final
print("ingrese notas de las Tareas:")
PT=float(input())
print("ingrese notas interrogaciones:")
PI=float(input())
print("ingrese notas examen:")
NE=float(input())
print("ingrese notas presentacion:")
PP=float(input())
print("ingrese promedio final: ")
PF= ((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))
PF=round(PF,1)
print("El promedio final es: ", PF)

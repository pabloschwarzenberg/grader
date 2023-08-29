#Nota final
PT = float(input("Ingrese nota por tareas:"))
PI = float(input("Ingrese nota por Interrogaciones:"))
NE = float(input("Ingrese nota por examenes:"))
PP = float(input("Ingrese nota por presentacion:"))
nota_final = 0.3*PT+0.3*PI+0.3*NE+0.1*PP
print("La nota final es:",nota_final)
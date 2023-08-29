#Nota final
print("Ingrese notas para calcular Nota Final")
PT = float(input("Tarea: "))
PI = float(input("Interrogaciones: "))
NE = float(input("Examen: "))
PP = float(input("Presentación: "))
NF = 0.3*PT+0.3*PI+0.3*NE+0.1*PP
print("La Nota Final es: {0} ".format(round(NF,1)))
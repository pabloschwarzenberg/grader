#Nota final 
print ("Ingrese sus notas ")
PT = float(input ("Ingrese notas de Tarea: "))
PI = float(input ("Ingrese notas de Interrogaciones: "))
NE = float(input ("'Ingrese nota de Examen: "))
PP = float(input ("Ingrese nota de Presentacion: "))
NP = (0.3*PT+0.3*PI+0.3*NE+0.1*PP)
print("La nota de presentacion es: ","{:.1f}".format(NP))
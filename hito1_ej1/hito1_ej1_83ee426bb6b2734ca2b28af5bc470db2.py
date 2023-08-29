      #Nota Final
PT=float(input("Ingrese nota de las tareas: "))
PI=float(input("Ingrese nota de las interrogaciones: "))
NE=float(input("Ingrese nota del examen: "))
PP=float(input("Ingrese nota de presentación: "))

#Desarrollo#
promedio=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print("El prmedio final es: ", round(promedio, 1))
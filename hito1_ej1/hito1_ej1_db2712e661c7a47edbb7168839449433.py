#Nota final
PT = float(input("Ingrese nota de TAREAS: "))
PI = float(input("Ingrese nota de INTERROGACIONES: "))
NE = float(input("Ingrese nota de EXAMEN: "))
PP = float(input("Ingrese nota de PRESENTACIÓN: "))

promedio_final = ((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP))


print(round(promedio_final,1))

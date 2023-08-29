#Nota final
# Entrada
PT = float(input("Ingrese nota Tareas: "))
PI = float(input("Ingrese nota Interrogaciones: "))
NE = float(input("Ingrese nota Examen: "))
PP = float(input("Ingrese nota Presentaciones: "))

#####
nota_f = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

########

print("La nota final del curso es: ", round(nota_f,1))      
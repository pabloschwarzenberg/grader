#Nota final

# ENTRADA
PT = float(input("Ingrese nota Tareas: "))
PI = float(input("Ingrese nota Interrogaciones: "))
NE = float(input("Ingrese nota Examen: "))
PP = float(input("Ingrese nota Presentaciones: "))
# PROCESAMIENTO
Nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
# SALIDA
print("La Nota final del curso es: ", round(Nota_final,1))
#Nota Final
PT = float(input("ingrese nota Tareas: "))

PI = float(input("ingrese nota Interrogaciones: "))

NE = float(input("ingrese nota Examen: "))

PP = float(input("ingrese nota Presentaciones : "))

N_F = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("La Nota Final del curso es: ", round(N_F,1))
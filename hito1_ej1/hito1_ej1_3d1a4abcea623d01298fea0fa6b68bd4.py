#Nota final
PT = float(input("ingrese nota Tareas:"))
PI = float(input("ingrese nota Interrogaciones:"))
NE = float(input("ingrese nota Examen:"))
PP = float(input("ingrese nota Presentacion:"))
R =0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
R2 = round(R,1)
print(R2)

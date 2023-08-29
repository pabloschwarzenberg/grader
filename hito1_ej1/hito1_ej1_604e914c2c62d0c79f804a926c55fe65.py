#Nota final
PT=float(input("Ingrese nota Tareas:"))
PI=float(input("Ingrese nota Interrogaciones:"))
NE=float(input("Ingrese nota Examen:"))
PP=float(input("Ingrese nota Presentación:"))
NF=float(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("Su promedio final es:",round(NF,1))
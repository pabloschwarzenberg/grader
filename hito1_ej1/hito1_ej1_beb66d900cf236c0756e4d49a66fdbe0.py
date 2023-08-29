#Nota final
PT = float(input("ingresa nota tarea:"))
PI = float(input("ingresa nota interrogante:"))
NE = float(input("ingresa nota examen:"))
PP = float(input("ingresa nota presentacion:"))
NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
NF1 = round(NF,1)
print("el promedio final es:",NF1)
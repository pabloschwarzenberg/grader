#Nota final
PT = float(input("ingrese la nota de las tareas:"))
PI = float(input("ingrese la nota de interrogaciones:"))
NE = float(input("ingrese la nota del examen:"))
PP = float(input("ingrese la nota de presentacion:"))
nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
nota_final = round(nota_final,1)
print(nota_final)
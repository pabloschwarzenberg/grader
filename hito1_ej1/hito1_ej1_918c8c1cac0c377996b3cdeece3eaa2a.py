#Nota final
PT=float(input("ingrese la nota de las tareas:"))
NE=float(input("ingrese la nota del examen:"))
PI=float(input("ingrese la nota de las interrogaciones:"))
PP=float(input("ingrese nota de presentacion:"))
#formula para sacar promedio
nota_final=round((0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP),1)
#promedio final
print("El promedio final es:",nota_final)
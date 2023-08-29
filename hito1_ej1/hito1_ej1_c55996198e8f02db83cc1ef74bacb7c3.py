#Nota final
#Nombre del creador: Daniel Ugarte
PT=float(input("ingrese notas de tareas:"))
PI=float(input("ingrese notas de interrogaciones:"))
NE=float(input("ingrese notas del examen:"))
PP=float(input("ingrese nota de presentacion:"))
nota_final=round((0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP),1)
print("su nota final corresponde a ",nota_final)
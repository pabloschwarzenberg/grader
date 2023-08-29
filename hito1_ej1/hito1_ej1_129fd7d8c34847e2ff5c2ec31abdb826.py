#Nota final
val_PT=float
val_PI=float
val_NE=float
val_PP=float
val_promedionotas=float

val_PT = float(input("ingrese nota tarea:"))
val_PI = float(input("ingrese nota interrogacion:")) 
val_NE = float(input("ingrese nota examen:"))
val_PP = float(input("ingrese nota presentacion:"))

val_PT = round((val_PT*0.30),1)
val_PI = round((val_PI*0.30),1)
val_NE = round((val_NE*0.30),1)
val_PP = round((val_PP*0.10),1)

val_promedionotas=round((val_PT + val_PT + val_NE + val_PP),1)

print ("El promedio de notas obtenido es:", format(val_promedionotas))
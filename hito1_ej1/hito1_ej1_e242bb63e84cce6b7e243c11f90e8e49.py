#Nota final
val_PT= float(input("Evaluacion Tarea :"))
val_PI= float(input("Evaluacion Interrogaciones :"))
val_NE= float(input("Evaluacion Examen:"))
val_PP= float(input("Evaluacion presentacion:"))



#promedio notas
Promedio= (val_PT*0.3 + val_PI*0.3 + val_NE*0.3+ val_PP*0.1)

nota_promedio = Promedio



#nota_presentacion 

print("{0:.1f}".format(nota_promedio) )


#Nota final
nota_1 = float(input("Ingresa nota tareas: "))
nota_2 = float(input("Ingresa nota interrogaciones: "))
nota_3 = float(input("Ingresa nota examen: "))
nota_4 = float(input("Ingresa nota presentacion: "))

promedio = round((nota_1*0.3) + (nota_2*0.3) + (nota_3*0.3) + (nota_4*0.1),1)

print ("El promedio final es", promedio)
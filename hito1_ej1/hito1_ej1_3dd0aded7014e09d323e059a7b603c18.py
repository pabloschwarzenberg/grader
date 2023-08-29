#Nota final
nota_tareas=float(input("Ingrese la nota de las tareas: "))
nota_ies=float(input("Ingrese sus nota de la interrogación: "))
nota_examen=float(input("Ingrese la nota de su examen: "))
nota_presentacion=float(input("Finalmente ingrese su nota de presentación: "))
nota_final=round(0.3*nota_tareas+0.3*nota_ies+0.3*nota_examen+0.1*nota_presentacion,1)
print("Su nota final del ramo es: ",nota_final)
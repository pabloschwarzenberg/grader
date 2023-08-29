print("---IMPORTANTE:TODAS LAS NOTAS DEBEN SER INGRESADAS EN DECIMALES---")
Tareas=float(input("Ingrese la nota de su tarea:"))
Interrogaciones=float(input("Ingrese la nota de sus Interrogaciones:"))
Examen=float(input("Ingrese la nota de su Examen:"))
Presentacion=float(input("Ingrese la nota de su presentacion:"))
porcentajeT= Tareas*0.3
porcentajeI= Interrogaciones*0.3
porcentajeE= Examen*0.3
porcentajeP= Presentacion*0.1
Notafinal=porcentajeP+porcentajeE+porcentajeI+porcentajeT
redondeado=round(Notafinal,1)
print("su nota final es:", redondeado)
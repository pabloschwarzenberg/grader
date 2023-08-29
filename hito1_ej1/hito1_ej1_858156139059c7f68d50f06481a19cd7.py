#Nota final
Pt = float(input("Ingrese la nota de las tareas : "))
Pi = float(input("Ingrese la nota de las interrogaciones: "))
NE = float(input("Ingrese la nota de los examenes: "))
PP = float(input("Ingrese la nota de la presentacion: "))
promedio = (Pt*0.3+Pi*0.3+NE*0.3+PP*0.1)
print(round(promedio,1))
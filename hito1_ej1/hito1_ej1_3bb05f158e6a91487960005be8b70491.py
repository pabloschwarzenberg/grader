#Nota final
PT= eval(input("Ingrese Nota de Tareas: "))
PI= eval(input("Ingrese Nota de Interrogaciones: "))
NE= eval(input("Ingrese Nota de Examen: "))
PP= eval(input("Ingrese Nota de Presentacion: "))
p= (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print("Su promedio final es: ",round(p,1))     
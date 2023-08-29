#Nota final
Tarea=float(input("Ingrese su nota de tarea : "))
Interrogaciones=float(input("Ingrese su nota de programacion : "))
Examen=float(input("Ingrese su nota del examen: "))
Presentacion=float(input("Ingrese su nota de presentacion :"))
promedio=Tarea*0.3 + Interrogaciones*0.3 + Examen*0.3 + Presentacion*0.1 
print("Su promedio es de :" ,round(promedio,1))    
#Nota final
a = eval(input("Ingrese Nota tareas: "))
b = eval(input("Ingrese Nota Interrogaciones: "))
c = eval(input("Ingrese Nota Examen: "))
d = eval(input("Ingrese Nota Presentacion: "))
promedio_final = (0.3*a)+(0.3*b)+(0.3*c)+(0.1*d)
print("El promedio final es de: %.1f" %promedio_final)
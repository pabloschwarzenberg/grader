#Nota final
pt = eval(input("ingrese la nota de las tareas: "))
pi = eval(input("ingrese la nota de interrogacion: "))
ne = eval(input("ingrese la nota del examen: "))
pp = eval(input("ingrese la nota de la presentacion: "))
promedio = (pt*0.3+pi*0.3+ne*0.3+pp*0.1)
print("tu promedio final es: ",(round(promedio,2)))  
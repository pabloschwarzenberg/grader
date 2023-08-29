pt= float(input("ingrese la nota de las tareas:"))
pi=float(input("ingrese la nota de las interrogaciones"))
ne=float(input("ingrese la nota del examen"))
pp=float(input("ingrese la nota de presentacion"))

promedio= (0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)
promedio_final= round(promedio, 1)
print("el promedio final es",promedio_final)
      
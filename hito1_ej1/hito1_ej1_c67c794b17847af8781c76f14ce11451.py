print("ingreso de notas. ")
pt=float(input("ingrese la nota de tareas: "))
pi=float(input("ingrese la nota de interrogaciones: "))
ne=float(input("ingrese la nota de interrogaciones: "))
pp=float(input("ingrese la nota de presentacion: "))

promedio= (pt*0.3+pi*0.3+ne*0.3+pp*0.1)

print("el promedio final es de",round(promedio,1))
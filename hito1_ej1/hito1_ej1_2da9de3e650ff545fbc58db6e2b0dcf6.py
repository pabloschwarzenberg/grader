#Nota final
pt=float(input("ingrese su nota de las tareas: "))
po=float(input("ingrese su nota de las interrogaciones"))
ne=float(input("ingrese su nota de las examen: "))
pp=float(input("ingrese su nota de las presentacion: "))
promedio=round((0.3*(pt)+(0.3*po)+(0.3*ne)+(0.1*pp)),1)

print("su promedio es", promedio)
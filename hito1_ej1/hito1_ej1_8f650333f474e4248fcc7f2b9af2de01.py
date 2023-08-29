#Nota final
pt=float(input("ingresa notas de tareas:"))
pi=float(input("ingresa tu nota de interrogaciones:"))
ne=float(input("ingresa tu nota del examen:"))
pp=float(input("ingresa la nota de presentacion:"))

promedio=round((0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp),1)

print("tu nota final es ",promedio)
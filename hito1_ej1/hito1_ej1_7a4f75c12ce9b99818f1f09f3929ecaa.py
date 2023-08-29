#Nota final
print("Ingresa tus 4 notas para calcular el promedio:")
pt = float(input("Nota de tarea: "))
pi = float(input("Nota de interrogaciones: "))
ne = float(input("Nota de examen: "))
pp = float(input("Nota de presentación "))
pf = (pt*0.3 + pi*0.3 + ne*0.3 + pp*0.1)
redondeo = round(pf, 1)
print("Su nota final es:", redondeo)
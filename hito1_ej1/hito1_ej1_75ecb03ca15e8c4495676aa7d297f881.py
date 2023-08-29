#Nota final

print("Utilizar notas con décimales con punto (.) y no coma (,)")
pt = float(input("Ingresa tu nota de tarea: "))
pi = float(input("Ingresa tu nota de interrogaciones: "))
ne = float(input("Ingresa tu nota de examen: "))
pp = float(input("Ingresa tu nota de presentacion: "))

nfinal = round(pt*30/100 + pi*30/100 + ne*30/100 + pp*10/100,1)

print("Tu promedio final es ",nfinal)
#Nota final
pt = float(input("ingrese nota de tarea: "))
pi = float(input("ingrese nota de interrogaciones: "))
ne = float(input("ingrese nota de exámen: "))
pp = float(input("ingrese nota de presentación: "))
#operatoria
promedio = pt*0.3 + pi*0.3 + ne*0.3 + pp*0.1
print(round(promedio, 1))

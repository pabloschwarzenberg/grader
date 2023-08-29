# calcular promedio de 4 notas con distinto porcentaje

pt = float(input("ingrese Nota de Tareas: "))
pi = float(input("ingrese Nota de Interrogaciones: "))
ne = float(input("ingrese Nota de Examen: "))
pp = float(input("ingrese Nota de Presentacion: "))

promedio = (pt*0.3)+(pi*0.3)+(ne*0.3)+(pp*0.1)
#promedio = promedio/4
promedio = round(promedio,1)
print(promedio)
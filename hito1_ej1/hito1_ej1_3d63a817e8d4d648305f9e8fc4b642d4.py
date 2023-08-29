#Nota final
#Entradas
pt = float(input("ingrese nota de Tareas (PT): "))
pi = float(input("ingrese nota de Interrogaciones (PI): "))
ne = float(input("ingrese nota de Examen (NE): "))
pp = float(input("ingrese nota de Presentación (PP): "))

#Cálculo
promedio = float((pt*0.3)+(pi*0.3)+(ne*0.3)+(pp*0.1))
promedio = round(promedio,1)

#Salida
print("El Promedio Final es:", promedio)
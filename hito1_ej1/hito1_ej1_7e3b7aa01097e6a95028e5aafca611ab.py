#Nota final
pt=float(input("inserte nota tareas: "))
pi=float(input("inserte nota interrogaciones: "))
ne=float(input("inserte nota de examen: "))
pp=float(input("inserte nota de presentacion: "))

promedio=((pt*0.3)+(pi*0.3)+(ne*0.3)+(pp*0.1))
promedio=round(promedio,1)
print(promedio)
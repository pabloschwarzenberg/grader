#Nota final
pt=float(input("Ingresa tu nota de tareas : "))
pi=float(input("Ingresa tu nota de interrogaciones : "))
ne=float(input("Ingresa tu nota de examenes : "))
pp=float(input("Ingresa tu nota de presentacion : "))

promedio_final = round((pt*0.3)+(pi*0.3)+(ne*0.3)+(pp*0.1), 1 )
print(promedio_final)
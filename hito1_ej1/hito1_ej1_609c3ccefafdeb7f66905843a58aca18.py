#Nota final
pt=float(input('infrese nota tarea: '))
pi=float(input('infrese nota interrogacion: '))
ne=float(input('infrese nota examen: '))
pp=float(input('infrese nota presentacion: '))
promedio=((pt*0.3)+(pi*0.3)+(ne*0.3)+(pp*0.1))
decimal=round(promedio,1)
print(decimal)
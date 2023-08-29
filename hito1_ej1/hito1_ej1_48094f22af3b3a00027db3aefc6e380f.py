#Nota final
#Entradas
pt=float(input("ingresa evaluación de la tarea: "))
pi=float(input("ingresa evaluación de las interrogaciones: "))
ne=float(input("ingresa evaluación del examen: "))
pp=float(input("ingresa evaluación de la presentación: "))

#Proceso

Nota_Final= float(round((pt*0.3 + pi*0.3 + ne*0.3 + pp*0.1),1))

#Salida
print(Nota_Final)
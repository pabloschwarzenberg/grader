#Nota final
pt=float(input("Ingresa tu nota de tareas  "))
pi=float(input("Ingresa tu nota de interrogaciones  "))
ne=float(input("Ingresa tu nota de examenes  "))
pp=float(input("Ingresa tu nota de presentacion "))

promedio_final= round((pt+pi+ne+pp)/ 4,2 )
print("promedio final es :",promedio_final)
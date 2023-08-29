#Nota final
tareas=          float(input("ingresarPT:"))
interrogaciones= float(input("ingresarPI:"))
examen=          float(input("ingresarNE:"))
presentacion=    float(input("ingresarPP:"))


promedio= 0.3*tareas + 0.3*interrogaciones + 0.3*examen + 0.1*presentacion
redondeado= round (promedio,1)
print (redondeado)

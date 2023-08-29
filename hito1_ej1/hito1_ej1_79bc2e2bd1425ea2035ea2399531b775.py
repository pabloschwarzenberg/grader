#Nota final
pt = float (input ("ingrese promedio tareas de trabajos: "))
pi = float (input ("ingrese promedio interrogaciones: "))
ne = float (input ("ingrese promedio notas de examen: "))
pp = float (input ("ingrese promedio de presentaciones: "))

prom = (0.3*pt+0.3*pi+0.3*ne+0.1*pp)
print ("su promedio final es", round(prom,1))
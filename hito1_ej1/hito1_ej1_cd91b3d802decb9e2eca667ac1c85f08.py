#Nota final
PT = input ("Ingresar nota por tareas: ")
PI = input ("Ingresar nota de interrogaciones ")
NE = input ("Ingresar nota de examen: ")
PP = input ("Ingresar nota de presentación: ")
promedio_Final = (0.3*float (PT))+(0.3*float(PI))+0.3*float (NE)+(0.1*float (PP))
print ("El promedio final es: ", round(promedio_Final,1))
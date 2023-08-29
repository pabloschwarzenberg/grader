#Nota final
PT= float(input("Ingresa la nota de las tareas"))
PI= float(input("Ingresa la nota de las Interrogaciones"))
NE= float(input("Ingresa la nota del Examen"))
PP= float(input("Ingresa la nota de la Presentacion"))



pf= 0.3*PT+0.3*PI+0.3*NE+0.1*PP

redondeo= round(pf,1)
print(redondeo)
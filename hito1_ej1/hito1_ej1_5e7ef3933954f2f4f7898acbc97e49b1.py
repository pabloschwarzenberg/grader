#Nota final
pt= float (input("ingrese promedio de tareas:"))
pl= float (input ("ingrese promedio de interrogaciones:"))
ne= float (input ("ingrese nota de examen:"))
pp= float (input ("ingrese nota presentacion:"))

notafinal= 0.3 * pt + 0.3 * pl + 0.3 * ne + 0.1 * pp

print (round(notafinal,1))  
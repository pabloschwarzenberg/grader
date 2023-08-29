#Nota final
pt= float(input('ingrese la nota de las tareas'))  
pi= float(input('ingrese la nota de las interrogaciones'))
ne= float(input('ingrese la nota del examen'))
pp= float(input('ingrese la nota de la presentacion'))

pf = ((0.3*pt)+ (0.3*pi) + (0.3*ne) + (0.1*pp))

print ('el promedio final es', round(pf, 1))

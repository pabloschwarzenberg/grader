#Nota final
pt= float(input('introdusca la nota de las tareas: '))
pi= float(input('introdusca la nota de las interrogaciones: '))
ne= float(input('introdusca la nota del examen: '))
pp= float(input('introdusca la nota de la presentacion: '))

pf= 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
pf=round(pf,1)

print('el promedio final es ',pf,)
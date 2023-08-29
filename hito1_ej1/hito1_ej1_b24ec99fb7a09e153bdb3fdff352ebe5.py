#Nota final
pt = eval(input("Ingrese las notas de su tarea:"))
pi = eval(input("Ingrese las notas de su interrogaciones:"))
ne = eval(input("Ingrese las notas de su examen:"))
pp = eval(input("Ingrese las notas de su presentacion:"))

pf = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp

print("{0:.1f}".format(pf))      
#Nota final
print ("ingrese Notas")

pt = float(input("nota tarea: "))
pi = float(input("nota interrogacion: "))
ne = float(input("nota examen: "))
pp = float(input("nota presentacion: "))

Nota_final= (0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)

print ('Nota final', "{: .1f}".format(Nota_final))
 



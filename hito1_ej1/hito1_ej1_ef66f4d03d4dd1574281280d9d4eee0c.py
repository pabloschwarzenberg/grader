pt = eval(input("ingrese la nota de las tareas: "))
pi = eval(input("ingrese la nota de las interrogaciones: "))
ne = eval(input("ingrese la nota de las examenes: "))
pp = eval(input("ingrese la nota de la presentacion: "))
nota = (0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
nota_1 = round((nota),1)
print (nota_1)
#Nota final
print("Debe ingresar sus notas para calcular su promedio final")
pt = eval(input("Ingrese su nota de las tareas: "))
pi = eval(input("Ingrese su nota de las interrogaciones: "))
ne = eval(input("Ingrese su nota del examen: "))
pp = eval(input("Ingrese su nota de la presentacion: "))

pf=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)

if pt>0 and pi>0 and ne>0 and pp>0:
    print("Su promedio final es: ", pf)
else:
    print("Opcion no valida")
      
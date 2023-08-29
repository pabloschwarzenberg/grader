ingreso = eval(input("el ingreso: "))
a_nac= eval(input("ingrese año de nacimiento: "))
n_hijos= eval(input("ingresar cantidad de hijos: "))
antiguedad= eval(input("ingrese tiempo en años en el banco: "))
e_civil= input("indique su estado civil (S/C): ")
ubicacion= input("Indidcar si reside en campo o ciudad(U/R) ")

edad= 2020-a_nac

if antiguedad>10 and n_hijos >=2:
    print("Aprobado")
elif e_civil=="C" and n_hijos > 3 and edad >=45 and edad<=55:
    print("Aprobados")
elif ingreso>2500000 and e_civil=="S" and ubicacion=="U":
    print("Aprobado")
elif ingreso>3500000 and antiguedad > 5:
    print("Aprobado")
elif ubicacion=="R" and e_civil=="C" and n_hijos<2:
    print("Aprobado")
else: print("Rechazado")
#en el python de mi pc le da correcto al verificar los errores que indica la pagina
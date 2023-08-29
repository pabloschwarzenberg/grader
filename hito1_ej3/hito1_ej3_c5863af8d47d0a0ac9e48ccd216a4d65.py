#Aprobación de créditos
ingreso=eval(input("ingres su ingreso:"))
a_nac=eval(input("ingrese año de nacimiento:"))
n_hijos=eval(input("ingres numero de hijos: "))
antiguedad=eval(input("ingres años de antiguedad en el banco:"))
e_civil=input("indique su estado cvil (S/C):")
ubicacion=input("indique si vive en campo o ciudad (U/R)")

edad=2020-a_nac

if antiguedad>10 and n_hijos >=2:
    print("APROBADO")
elif e_civil=="C" and n_hijos > 3 and edad>=45 and edad<=55:
    print("APROBADO")
elif ingreso>2500000 and e_civil=="S" and ubicacion=="U":
    print("APROBADO")
elif ingreso>3500000 and antiguedad >5:
    print("APROBADO")
elif ubicacion=="R" and e_civil=="C" and n_hijos<2 :
    print("APROBADO")
else:print("RECHAZADO")     
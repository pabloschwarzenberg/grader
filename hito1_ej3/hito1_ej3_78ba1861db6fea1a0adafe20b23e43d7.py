#Aprobación de créditos
ingreso=eval(input("Ingrese su INGRESO: "))
a_nac=eval(input("Ingrese año de nacimiento:"))
n_hijos=eval(input("Ingrese numero de hijos:"))
antiguedad=eval(input("Ingrese año de antiguedad en el banco: "))
e_civil=input("Indique su estado civil (S/C): ")
ubicacion=input("Indique si vive en zona urbana o rural (U/R): ")
edad=2020-a_nac

if antiguedad>10 and n_hijos >=2:
    print("APROBADO")
elif e_civil=="C" and n_hijos > 3 and edad>=45 and edad<=55 :
    print("APROBADO")
elif ingreso>2500000 and e_civil=="S" and ubicacion=="U":
    print("APROBADO")
elif ubicacion=="R" and e_civil=="C" and n_hijos<2 :
    print("APROBADO")
else:print("RECHAZADO")


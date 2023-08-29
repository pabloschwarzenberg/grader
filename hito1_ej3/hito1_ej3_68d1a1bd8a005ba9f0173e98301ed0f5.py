#Aprobación de créditos
ingreso=eval(input("ingres su ingreso:"))
añonac=eval(input("ingrese año de nacimiento:"))
numhijos=eval(input("ingres numero de hijos: "))
antiguedad=eval(input("ingres años de antiguedad en el banco:"))
estcivil=input("indique su estado cvil (S/C):")
ubicacion=input("indique si vive en campo o ciudad (U/R)")

edad=2020-añonac

if antiguedad>10 and numhijos >=2:
    print("APROBADO")
elif estcivil=="C" and numhijos > 3 and edad>=45 and edad<=55:
    print("APROBADO")
elif ingreso>2500000 and estcivil=="S" and ubicacion=="U":
    print("APROBADO")
elif ingreso>3500000 and antiguedad >5:
    print("APROBADO")
elif ubicacion=="R" and estcivil=="C" and numhijos<2 :
    print("APROBADO")
else:
    print("RECHAZADO")
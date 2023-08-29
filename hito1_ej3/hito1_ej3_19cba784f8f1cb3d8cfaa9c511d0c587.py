#Aprobación de créditos
INGRESOS=eval(input("Introduzca sus ingresos:"))
AN=eval(input("Ingrese año de nacimiento:"))
HIJOS=eval(input("Ingrese numero de hijos: "))
AB=eval(input("Ingrese años de antiguedad en el banco:"))
EC=input("Indique su estado cvil (S/C):")
VIVIENDA=input("Indique si vive en campo o ciudad (U/R)")

EDAD=2020-AN

if AB>10 and HIJOS >=2:
    print("APROBADO")
elif EC=="C" and HIJOS > 3 and EDAD>=45 and EDAD<=55:
    print("APROBADO")
elif INGRESOS>2500000 and EC=="S" and VIVIENDA=="U":
    print("APROBADO")
elif INGRESOS>3500000 and AB >5:
    print("APROBADO")
elif VIVIENDA=="R" and EC=="C" and HIJOS<2 :
    print("APROBADO")
else:
    print("RECHAZADO")
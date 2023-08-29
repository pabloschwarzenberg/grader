#Aprobación de créditos
Ingreso=input("De su ingreso mensual")
AñoN=input("Año de nacimiento")
Hijos=input("Nùmero de hijos")
AñoB=input("Años banco")
Estadocivil=input("soltero o casado(S o C)")

Vivienda=input("Campo o ciudad (R o U)")
Ingreso=int(Ingreso)
AñoN=int(AñoN)
Hijos=int(Hijos)
AñoB=int(AñoB)
Edad=int(2017-AñoN)

if AñoB>10 and 2<=Hijos:
  print("APROBADO")
elif Estadocivil=="C" and Hijos>3 and 45<Edad<55:
    print("APROBADO")
elif Ingreso>2500000 and Estadocivil=="S" and Vivienda=="U":
    print("APROBADO")
elif Ingreso>3500000 and AñoB>5:
    print("APROBADO")
elif Vivienda=="R" and Estadocivil=="C" and Hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")


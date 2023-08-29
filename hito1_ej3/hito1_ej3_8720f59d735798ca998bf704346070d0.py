#Aprobación de créditos
ingreso=int(input())
nacimiento=int(input())
hijos=int(input())
tiempo=int(input())
estadocivil=input()
lugar=input()
edad=2018-nacimiento
C="casado"
S="soltero"
U="urbano"
R="rural"
if tiempo>10 or hijos==2:
 print("APROBADO")
else:
 if estadocivil==C or hijos>=3 or 45<=edad<=55:
  print("APROBADO")
 else:
  if ingreso>2500000 or estadocivil==S or lugar==U:
   print("APROBADO")
  else:
   if ingreso>3500000 or tiempo>5:
    print("APROBADO")
   else:
    if lugar==C or estadocivil==C or hijos<2:
     print("APROBADO")
    else:
     print("RECHAZADO")

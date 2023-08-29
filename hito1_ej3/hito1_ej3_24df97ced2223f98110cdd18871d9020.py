#Aprobación de créditos
ingreso=int(input("cuales son sus ingresos?"))
nacimiento=int(input("ingrese su año de nacimiento"))
hijos=int(input("numero de hijos"))
banco=int(input("años de pertenencia al banco"))
civil=input("estado civil Soltero 'S' o Casado 'C'")
lugar=input("'U' Urbano o 'C' Ciudad")
actualidad=2018
edad=actualidad-nacimiento

if banco>10 and hijos >= 2:
  print("APROBADO")
if civil=="C" and hijos>3 and edad>=45 and edad <=55:
  print("APROBADO")
if ingreso>3500000 and banco>5:
  print("APROBADO")
if ingreso>2500000 and civil=="S" and lugar=="C":
  print("APROBADO")
if lugar=="U" and civil=="C" and hijos<2:
  print("APROBADO")
else:
  print("NO APROBADO")

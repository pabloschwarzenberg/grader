#Aprobación de créditos
ingreso=int(input())
año=int(input())
hijos=int(input())
AB=int(input())
EC=input()
vivienda=input()
edad=2018-año
if (AB>10 and hijos>=2) or (EC=="C" and hijos>3 and 45<=edad<=55) or (ingreso>2500000 and EC=="S" and vivienda=="U") or (ingreso>3500000 and AB>5) or (vivienda=="R" and EC=="C" and hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")
#Aprobación de créditos
ingreso=int(input())
edad=int(input())
hijos=int(input())
anosbanco=int(input())
ecivil=str(input())
residencia=str(input())
if anosbanco>10 and hijos>=2:
  print("APROBADO")
elif ecivil=="C" and hijos>3 and 45<edad<55:
  print("APROBADO")
elif ingreso>2500000 and ecivil==S and residencia==U:
  print("APROBADO")
elif ingreso>3500000 and anosbanco>5:
  print("APROBADO")
elif residencia=="R" and ecivil=="C" and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")
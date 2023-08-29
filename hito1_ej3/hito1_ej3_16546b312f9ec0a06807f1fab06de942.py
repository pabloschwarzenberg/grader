#Aprobacion de creditos
ingresos=int(input("ingrese su sueldo: $"))
año=int(input("ingrese el año de su nacimiento: "))
nhijos=int(input("numero de hijos: "))
añosb=int(input("años de pertenencia en el banco: "))
ecivil=str(input("ingrese su estado civil {(S) si esta soltero, (C) si esta casado}: "))
vivienda=str(input("ingrese si su recidencia se encuentra en el campo o la ciudad {Campo=(R), Ciudad=(U)}: "))
edad=(2020-año)
if(añosb>=10 and nhijos>=2) or (ecivil=="C" and nhijos>3 and 45<=edad<=55) or (ingresos>2500000 and ecivil=="S" and vivienda=="U") or (ingresos>3500000 and añosb>5) or (vivienda=="R" and ecivil=="C" and nhijos<2):
 print("APROBADO")
else:
  print("RECHAZADO")
#Aprobación de créditos
ingreso=int(input())
nacimiento=int(input())
hijos=int(input())
pertenencia=int(input())
estado=input()
campciud=input()
edad=2017-nacimiento

if ((pertenencia>10 and hijos>=2) or
   (estado=="C" and hijos>3 and 45>edad>55) or
   (ingreso>2500000 and estado=="S" and campciud=="U") or
   (ingreso>3500000 and pertenencia>5) or
   (campciud=="R" and estado=="C" and hijos<2)):
     print("APROBADO")
else:
  print("RECHAZADO")
#Aprobación de créditos
ingreso=int(input())
nacimiento=int(input())
hijos=int(input())
pertenencia=int(input())
estado=input()
sector=input()
edad=2018-nacimiento

if(((pertenencia>10) and (hijos>=2)) or ((estado=="C") and (hijos>=3) and (45<=edad<=55)) or ((ingreso>2500000) and (estado=="C") and (sector=="U")) or ((ingreso>3500000) and (pertenencia>5)) or ((sector=="R") and (estado=="C") and (hijos<2))):
   print("APROBADO")
else:
   print("NO APROBADO")
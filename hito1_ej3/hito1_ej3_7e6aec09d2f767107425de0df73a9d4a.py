#Aprobación de créditos
ingreso=int(input())
nacimiento=int(input())
hijos=int(input())
pertenencia=int(input())
estado=input()
ubicacion=input()
edad=2018-nacimiento

if(((pertenencia>10) and (hijos>=2)) or ((estado=="C") and (hijos>=3) and (45<=edad<=55)) or ((ingreso>2500000) and (estado=="C") and (ubicacion=="U")) or ((ingreso>3500000) and (pertenencia>5)) or ((ubicacion=="R") and (estado=="C") and (hijos<2))):
   print("APROBADO")
else:
   print("RECHAZADO")

#Aprobación de créditos
ingreso=int(input())
ddn=int(input())
hijos=int(input())
pertenencia=int(input())
estado=str(input())
lugar=str(input())

ano=2017-ddn

if(ingreso>=2500000 and estado=="S" and lugar=="U"):
   print("APROBADO")
elif(pertenencia>=10 and hijos>=2):
   print("APROBADO")
elif(ano>45 and ano<55 and estado=="C" and hijos>3):
   print("APROBADO")
elif(ingreso>=3500000 and pertenencia>=5):
   print("APROBADO")
elif(lugar=="R" and estado=="C" and hijos<3):
   print("APROBADO")
else:
   print("NO APROBADO")
#Aprobación de créditos
ing=int(input())
edad=int(input())
edad=(2018-edad)
nh=int(input())
apb=int(input())
ec=str(input())
caci=str(input())
if ((apb>=10) and (nh>=2)) or ((nh>3) and ((45<=edad) or (edad<=55))) or ((ing>=2500000) and (ec=="S") and (caci=="U")) or ((ing>=3500000) and (apb>5)) or ((caci=="R") and (ec=="C")and (nh<2)):
  print("APROBADO")
else:
  print("RECHAZADO")
#Zodiaco
#Estoy seguro de que hay una mejor manera de hacer esto >.<
Dia=int(input("Ingrese el dia: "))
Mes=int(input("Ingrese el mes: "))

if (Mes==1) and (Dia<=20): 
  print("Capricornio")
if (Mes==1) and (20<Dia<=31):
  print("Acuario")

if (Mes==2) and (Dia<=19):
  print("Acuario")
if (Mes==2) and (19<Dia<=29):
  print("Piscis")
  
if (Mes==3) and (Dia<=20):
  print("Piscis")
if (Mes==3) and (20<Dia<=31):
  print("Aries")
  
if (Mes==4) and (Dia<=20):
  print("Aries")
if (Mes==4) and (20<Dia<=30):
  print("Tauro")
  
if (Mes==5) and (Dia<=21):
  print("Tauro")
if (Mes==5) and (21<Dia<=31):
  print("Gemini")
  
if (Mes==6) and (Dia<=21):
  print("Gemini")
if (Mes==6) and (21<Dia<=30):
  print("Cancer")
  
if (Mes==7) and (Dia<=22):  
  print("Cancer")
if (Mes==7) and (22<Dia<=31):
  print("Leo")
  
if (Mes==8) and (Dia<=23):  
  print("Leo")
if (Mes==8) and (23<Dia<=31):
  print("Virgo")
  
if (Mes==9) and (Dia<=23):  
  print("Virgo")
if (Mes==9) and (23<Dia<=30):  
  print("Libra")
  
if (Mes==10) and (Dia<=23):
  print("Libra")
if (Mes==10) and (23<Dia<=31):
  print("Escorpión")
  
if (Mes==11) and (Dia<=22):
  print("Escorpión")
if (Mes==11) and (22<Dia<=30):
  print("Sagitario")
  
if (Mes==12) and (Dia<=21):
  print("Sagitario")
if (Mes==12) and (21<Dia<31):
  print("Acuario")
  
else: print("Fecha no válida")
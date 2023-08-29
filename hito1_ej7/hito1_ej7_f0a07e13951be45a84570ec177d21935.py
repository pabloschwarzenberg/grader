#Zodiaco
dia=int(input("ingrese dia de cumpleaños"))
mes=int(input("ingrese mes de cumpleaños"))
 
if (mes==3) and (dia>=21) or (mes==4) and (dia<=21):
  print("aries")
elif (mes==4) and (dia>=21) or (mes==5) and (dia<=21):
  print("taurus")
elif (mes==5) and (dia>=21) or (mes==6) and (dia<=21):
  print("gemini")
elif (mes==6) and (dia>=21) or (mes==7) and (dia<=23):
  print("cancer")
elif (mes==7) and (dia>=23) or (mes==8) and (dia<=23):
  print("leo")
elif (mes==8) and (dia>=23) or (mes==9) and (dia<=23):
  print("virgo")
elif (mes==9) and (dia>=23) or (mes==10) and (dia<=23):
  print("libra")
elif (mes==10) and (dia>=23) or (mes==11) and (dia<=23):
  print("escorpio")
elif (mes==11) and (dia>=23) or (mes==12) and (dia<=22):
  print("sagitario")
elif (mes==12) and (dia>=22) or (mes==1) and (dia<=20):
  print("capricornio")
elif (mes==1) and (dia>=20) or (mes==2) and (dia<=19):
  print("aquario")
elif (mes==2) and (dia>=19) or (mes==3) and (dia<=21):
  print("piscis")      
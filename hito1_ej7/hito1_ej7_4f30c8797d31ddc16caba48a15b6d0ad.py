#Zodiaco
dia=int(input("ingresenel dia: "))
mes=int(input("ingrese el mes: "))
if (dia>=21 and mes==3) or (dia<=20 and mes==4):
  print("aries")
if (dia>=21 and mes==4) or (dia<=20 and mes==5):
  print("tauro")
if (dia>=21 and mes==5) or (dia<=21 and mes==6):
  print("gemini")
if(dia>=22 and mes==6) or (dia<=22 and mes==7):
  print("cancer")
if(dia>=23 and mes==7) or (dia<=22 and mes==8):
  print("leo")
if(dia>=23 and mes==8) or (dia>=22 and mes<=9):
  print("virgo")
if (dia>=23 and mes==9) or (dia<=22 and mes==10):
  print("libra")
if(dia>=23 and mes==10) or (dia<=22 and mes==11):
  print("escorpio")
if(dia>=23 and mes==11) or (dia<=21 and mes==12):
  print("sagittario")
if(dia>=22 and mes==12) or (dia<=20 and mes==1):
  print("capricornio")
if(dia>=21 and mes==1) or (dia<=18 and mes==2):
  print("aquario")
if(dia>=19 and mes==2) or (dia<=20 and mes==3):
  print("piscis")
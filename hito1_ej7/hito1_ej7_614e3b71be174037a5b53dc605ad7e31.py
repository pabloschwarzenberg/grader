#Zodiaco
dia=0
while (dia<1 or dia>31):
  dia=int(input("Dia de cumpleaños: "))
mes=0
while (mes<1 or mes>12):
  mes=int(input("Mes de cumpleaños: "))

if (dia>=21 and mes==3 or dia<=20 and mes==4):
  print("tu signo del zodiaco es Aries")

elif (dia>=21 and mes==4 or dia<=21 and mes==5):
  print("tu signo del zodiaco es Tauro")

elif (dia>=22 and mes==5 or dia<=21 and mes==6):
  print("tu signo del zodiaco es Geminis")

elif (dia>=22 and mes==6 or dia<=23 and mes==7):
  print("tu signo del zodiaco es Cancer")

elif (dia>=24 and mes==7 or dia<=23 and mes==8):
  print("tu signo del zodiaco es Leo")

elif (dia>=23 and mes==8 or dia<=22 and mes==9):
  print("tu signo del zodiaco es Virgo")

elif (dia>=23 and mes==9 or dia<=22 and mes==10):
  print("tu signo del zodiaco es Libra")

elif (dia>=23 and mes==10 or dia<=22 and mes==11):
  print("tu signo del zodiaco es Escorpio")

elif (dia>=23 and mes==11 or dia<=22 and mes==12):
  print("tu signo del zodiaco es Sagitario")

elif(dia>=23 and mes==12 or dia<=20 and mes==1):
  print("tu signo del zodiaco es Capricornio")

elif(dia>=21 and mes==1 or dia<=18 and mes==2):
  print("tu signo del zodiaco es Acuario")

elif(dia>=19 and mes==2 or dia<=20 and mes==3):
  print("tu signo del zodiaco es Piscis")   
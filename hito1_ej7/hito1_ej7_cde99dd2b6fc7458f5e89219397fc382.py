#Zodiacodia 
dia = int(input("ingrese dia de cumpleaños: "))
mes = int(input("ingrese mes de cumpleaños: "))
#aries
if(dia>=21 and  mes == 3) or (dia<20 and mes==4):
  print("eres aries")
#tauro
if(dia>=20 and  mes == 4) or (dia<21 and mes==5):
  print("eres tauro")
#geminis
if(dia>=21 and mes == 5) or (dia<21 and mes==6):
  print("eres geminis")
#cancer
if(dia>=21 and mes == 6) or (dia<23 and mes==7):
  print("eres cancer")
#leo
if(dia>=23 and mes == 7) or (dia<23 and mes==8):
  print("eres leo")
#virgo
if(dia>=23 and mes == 8) or (dia<23 and mes==9):
  print("eres virgo")
#libra
if(dia>=23 and mes == 9) or (dia<=23 and mes==10):
  print("eres libra")
#escorpio 
if(dia>23 and mes == 10) or (dia<23 and mes==11):
  print("eres escorpio")
#sagitario
if(dia>=23 and mes == 11) or (dia<22 and mes==12):
  print("eres sagitario")
#capricornio
if(dia>=22 and mes == 12) or (dia<20 and mes==1):
  print("eres capricornio")
#acuario
if(dia>=20 and mes == 1) or (dia<19 and mes==2):
  print("eres acuario")
#piscis
if(dia>=19 and mes == 2) or (dia<21 and mes==3):
  print("eres piscis")
print("Ingrese datos de nacimiento:")
dia=int(input("dia nacimiento: "))
mes=int(input("mes nacimiento: "))
print("Fecha de nacimiento:",dia,"/",mes)
if(dia>=21 and mes==3 or dia<=20 and mes==4):
  print("Usted es ARIES")
elif(dia>=20 and mes==4 or dia<=21 and mes==5):
  print("Usted es TAURO")
elif(dia>=21 and mes==5 or dia<=21 and mes==6):
  print("Usted es GEMINIS")
elif(dia>=21 and mes==6 or dia<=22 and mes==7):
  print("Usted es CANCER")
elif(dia>=23 and mes==7 or dia<=23 and mes==8):
  print("Usted es LEO")
elif(dia>=23 and mes==8 or dia<=23 and mes==9):
  print("Usted es VIRGO")
elif(dia>=23 and mes==9 or dia<=23 and mes==10):
  print("Usted es LIBRA")
elif(dia>=23 and mes==10 or dia<=22 and mes==11):
  print("Usted es ESCORPIO")
elif(dia>=22 and mes==11 or dia<=22 and mes==12):
  print("Usted es SAGITARIO")
elif(dia>=22 and mes==12 or dia<=20 and mes==1):
  print("Usted es CAPRICORNIO")
elif(dia>=20 and mes==1 or dia<=19 and mes==2):
  print("Usted es ACUARIO")
elif(dia>=19 and mes==2 or dia<=21 and mes==3):
  print("Usted es PISCIS")
      
print("Ingrese fecha de nacimiento sin considerar el año:")
dia=int(input("dia de nacimiento: "))
mes=int(input("mes de nacimiento: "))
print("Fecha de nacimiento:",dia,"/",mes)
if(dia>=21 and mes==3 or dia<=20 and mes==4):
  print("Su signo es ARIES")
elif(dia>=20 and mes==4 or dia<=21 and mes==5):
  print("Su signo es TAURO")
elif(dia>=21 and mes==5 or dia<=21 and mes==6):
  print("Su sigo es GEMINIS")
elif(dia>=21 and mes==6 or dia<=22 and mes==7):
  print("Su signo es CANCER")
elif(dia>=23 and mes==7 or dia<=23 and mes==8):
  print("Su signo es LEO")
elif(dia>=23 and mes==8 or dia<=23 and mes==9):
  print("Su signo es VIRGO")
elif(dia>=23 and mes==9 or dia<=23 and mes==10):
  print("Su signo es LIBRA")
elif(dia>=23 and mes==10 or dia<=22 and mes==11):
  print("Su signo es ESCORPIO")
elif(dia>=22 and mes==11 or dia<=22 and mes==12):
  print("Su signo es SAGITARIO")
elif(dia>=22 and mes==12 or dia<=20 and mes==1):
  print("Su signo es CAPRICORNIO")
elif(dia>=20 and mes==1 or dia<=19 and mes==2):
  print("Su signo es ACUARIO")
elif(dia>=19 and mes==2 or dia<=21 and mes==3):
  print("Su signo es PISCIS")
      
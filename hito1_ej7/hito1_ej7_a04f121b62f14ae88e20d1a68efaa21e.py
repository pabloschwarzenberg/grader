#Zodiaco
dia=int(input("Ingresa el número del día de tu cumpleaños:"))
mes=int(input("Ingresa el número de tu mes:"))

if (dia>=21 and mes==3) or (dia<=20 and mes==4):
   print("Tu signo es Aries")
elif (dia>=21 and mes==4) or (dia<=21 and mes==5):
   print("Tu signo es Tauro")
elif (dia>=22 and mes==5) or (dia<=21 and mes==6):
   print("Tu signo es Géminis")
elif (dia>=22 and mes==6) or (dia<=22 and mes==7):
   print("Tu signo es Cáncer")
elif (dia>=23 and mes==7) or (dia<=22 and mes==8):
   print("Tu signo es Leo")
elif (dia>=23 and mes==8) or (dia<=23 and mes==9):
   print("Tu signo es Virgo")
elif (dia>=24 and mes==9) or (dia<=23 and mes==10):
   print("Tu signo es Libra")
elif (dia>24 and mes==10) or (dia<=22 and mes==11):
   print("Tu signo es Escorpión")
elif (dia>=23 and mes==11) or (dia<=21 and mes==12):
   print("Tu signo es Sagitario")
elif (dia>=22 and mes==12) or (dia<=20 and mes==1):
   print("Tu signo es Capricornio")
elif (dia>=21 and mes==1) or (dia<=19 and mes==2):
   print("Tu signo es Acuario")
elif (dia>20 and mes==2) or (dia<=20 and mes==3):
   print("Tu signo es Piscis")
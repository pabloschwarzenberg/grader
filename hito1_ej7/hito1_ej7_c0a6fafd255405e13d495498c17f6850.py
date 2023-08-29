#Zodiaco
dia=int(input("Ingrese el día que usted nacio: "))
mes=int(input("Ingrese el número correspondiente al mes que usted nacio: "))
if((dia>=21 and dia<32 and mes==3) or (dia<=20 and mes==4 )):
  print("Usted pertence al signo zodiacal: Aries")
elif((dia>=20 and dia<32 and mes==4) or (dia<=21 and mes==5)):
  print("Usted pertence al signo zodiacal: Tauro")
elif((dia>=21 and dia<32 and mes==5) or (dia<=21 and mes==6)):
 print("Usted pertence al signo zodiacal: Geminis")
elif((dia>=21 and dia<32 and mes==6) or (dia<=23 and mes==7)):
 print("Usted pertence al signo zodiacal: Cancer")
elif((dia>=23 and dia<32 and mes==7) or (dia<=23 and mes==8)):
 print("Usted pertence al signo zodiacal: Leo")
elif((dia>=23 and dia<32 and mes==8) or (dia<=23 and mes==9)):
 print("Usted pertence al signo zodiacal: Virgo")
elif((dia>=23 and dia<32 and mes==9) or (dia<=23 and mes==10)):
 print("Usted pertence al signo zodiacal: Libra")
elif((dia>=23 and dia<32 and mes==10) or (dia<=22 and mes==11)):
 print("Usted pertence al signo zodiacal: Escorpión")
elif((dia>=22 and dia<32 and mes==11) or (dia<=22 and mes==12)):
 print("Usted pertence al signo zodiacal: Sagitario")
elif((dia>=22 and dia<32 and mes==12) or (dia<=20 and mes==1)):
 print("Usted pertence al signo zodiacal: Capricornio")
elif((dia>=20 and dia<32 and mes==1) or (dia<=19 and mes==2)):
 print("Usted pertence al signo zodiacal: Acuario")
elif((dia>=19 and dia<29 and mes==2) or (dia<=21 and mes==3)):
 print("Usted pertence al signo zodiacal: Piscis")
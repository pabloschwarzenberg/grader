a= int(input("Escriba el dia de su cumpleaños: "))
mes= int(input("Escriba el mes de su cumpleaños: "))
a<=31
mes<=12

#Aries
if (a>=21 and a<20 and mes==3 or mes==4):
  print("Su signo es Aries")
#Tauro
elif (a>=20 and a<21 and  mes==4 or mes==5):
  print("Su signo es Tauro")
#Geminis 
elif (a>=21 and a<21 and  mes==5 or mes==6):
  print("Su signo es Geminis")
#Cancer
elif (a>=21 and a<23 and mes==6 or mes==7):
  print("Su signo es Cancer")
#Leo
elif (a>=23 and a<23 and  mes==7 or mes==8):
  print("Su signo es Leo")
#Virgo
elif (a>=23 and a<23 and  mes==8 or mes==9):
  print("Su signo es Virgo")
#Libra
elif (a>=23 and a<23 and  mes==9 or mes==10):
  print("Su signo es Libra")
#Scorpio
elif (a>=23 and a<22 and  mes==10 or mes==11):
  print("Su signo es Escorpión")
#Sagitario
elif (a>=23 and a<22 and  mes==11 or mes==12):
  print("Su signo es Sagitario")
#Capricornio
elif (a>=22 and a<20 and  mes==12 or mes==1):
  print("Su signo es Capricornio")
#Acuario
elif (a>=20 and a<19 and mes==1 or mes==2):
  print("Su signo es Acuario")
#Piscis
else:
  (a>=19 and a<21 and  mes==2 or mes==3)
  print("Su signo es Piscis")
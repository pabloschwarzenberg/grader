#Zodiaco
dia=int(input("Ingrese su dia de nacimiento"))
mes=int(input("Ingrese su mes de nacimiento"))
if (mes==1 and dia<=20 or mes==12 and dia>=22):
  print("Tu signo es Capricornio")
elif(mes==1 and dia<=20 or mes==2 and dia>=21):
  print("Tu signo es Acuario")
elif(mes==3 and dia<=22 or mes==2 and dia>=21):
  print("Tu signo es Piscis")
elif (mes==4 and dia<=20 or mes==3 and dia>=23):
  print("Tu signo es Aries")
elif (mes==5 and dia<=22 or mes==4 and dia>=21):
  print("Tu signo es Tauro")
elif (mes==6 and dia<=22 or mes==5 and dia>=23):
  print("Tu signo es Geminis")
elif (mes==7 and dia<=22 or mes==6 and dia>=23):
  print("Tu signo es Cancer")
elif (mes==8 and dia<=22 or mes==7 and dia>=23):
  print("Tu signo es Leo")
elif (mes==9 and dia<=22 or mes==8 and dia>=23):
  print("Tu signo es Virgo")
elif (mes==10 and dia<=22 or mes==9 and dia>=23):
  print("Tu signo es Libra")
elif (mes==11 and dia<=22 or mes==10 and dia>=23):
  print("Tu signo es Scorpio")
elif (mes==12 and dia<=21 or mes==12 and dia>=22):
  print("Tu signo es Sagitario")
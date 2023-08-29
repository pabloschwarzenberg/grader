#Zodiaco
dia = eval(input("ingrese el dia de su nacimiento: "))
mes = eval(input("ingrese el mes de su nacimiento: "))
if (mes==3 and dia>=21 ) or (mes==4 and dia<=20):
  print("tu signo zodiacal es aries")
if (mes==4 and dia>=21 ) or (mes==5 and dia<=21):
   print("tu signo zodiacal es tauro")
elif (mes==5 and dia>=22 ) or (mes==6 and dia<=21):
   print("tu signo zodiacal es geminis")
elif (mes==6 and dia>=22 ) or (mes==7 and dia<=22):
   print("tu signo zodiacal es cancer")
elif (mes==7 and dia>=23 ) or (mes==8 and dia<=22):
   print("tu signo zodiacal es leon")
elif (mes==8 and dia>=23 ) or (mes==9 and dia<=23):
   print("tu signo zodiacal es virgo")
elif (mes==9 and dia>=24 ) or (mes==10 and dia<=23):
   print("tu signo zodiacal es libra")
elif (mes==10 and dia>=24 ) or (mes==11 and dia<=22):
   print("tu signo zodiacal es escorpion")
elif (mes==11 and dia>=23 ) or (mes==12 and dia<=21):
   print("tu signo zodiacal es sagitario")
elif (mes==12 and dia>=22 ) or (mes==1 and dia<=20):
   print("tu signo zodiacal es capricornio")
elif (mes==1 and dia>=21 ) or (mes==2 and dia<=19):
   print("tu signo zodiacal es acuario")
elif (mes==2 and dia>=20 ) or (mes==3 and dia<=20):
   print("tu signo zodiacal es piscis")
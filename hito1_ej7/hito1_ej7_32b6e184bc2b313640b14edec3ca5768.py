#Zodiaco
#INPUT FECHA DE NACIMIENTO
dia=int(input("Ingrese el número del día en que nació"))
mes=int(input("Ingrese el mes en que nació"))
#DETERMINACIÓN DEL SIGNO ZODIACAL
if mes==1:
  if dia<=21:
    print("capricornio")
  else:
    print("acuario")
elif mes==2:
  if dia<=21:
    print("acuario")
  else:
    print("piscis")
elif mes==3:
  if dia<=23:
    print("piscis")
  else:
    print("aries")
elif mes==4:
  if dia<=21:
    print("aries")
  else:
    print("tauro")
elif mes==5:
  if dia<=21:
    print("tauro")
  else:
    print("geminis")
elif mes==6:
  if dia<=21:
    print("geminis")
  else:
    print("cáncer")
elif mes==7:
  if dia<=21:
    print("cáncer")
  else:
    print("leo")
elif mes==8:
  if dia<=22:
    print("leo")
  else:
    print("virgo")
elif mes==9:
  if dia<=21:
    print("virgo")
  else:
    print("libra")
elif mes==10:
  if dia<=21:
    print("libra")
  else:
    print("escorpio")
elif mes==11:
  if dia<=22:
    print("escorpio")
  else:
    print("sagitario")
elif mes==12:
  if dia<=21:
    print("sagitario")
else:
  print("capricornio")
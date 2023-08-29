#Zodiaco
día=int(input("ingresa el día de tu cumpleaños\n"))
mes=int(input("ingresa el mes de tu cumpleaños\n"))
fecha=mes*100+día
if (fecha>=321) and fecha <420:
  print("Aries")
elif fecha >=420 and fecha<521:
  print("Tauro")
elif fecha>=521 and fecha <621:
  print ("Géminis")
elif fecha>=621 and fecha <723:
  print("cancer")
elif fecha>=723 and fecha <823:
  print("León")
elif fecha>=823 and fecha <923:
  print ("Virgo")
elif fecha>=923 and fecha <1023:
  print("Libra")
elif fecha>=1023 and fecha <1124:
  print ("Escorpio")
elif fecha>=1124 and fecha <1222:
  print ("Sagitario")
elif (fecha>=1222 and fecha <1231) or (fecha>=11 and fecha<120):
  print ("Capricornio")
elif fecha>=120 and fecha<219:
  print ("Acuario")
elif fecha>=219 and fecha <321:
  print((Piscis))
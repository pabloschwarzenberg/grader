#Zodiaco
dia = int(input("dia -> "))
mes = int(input("mes -> "))

signo = int((mes*100) + dia)

print (signo)

if (221 <= signo <= 420):
  print("aries")
elif (421 <= signo <= 521):
  print("tauro")
elif (522 <= signo <= 621):
  print("geminis")
elif (622 <= signo <= 723):
  print("cancer")
elif (724 <= signo <= 823):
  print("leo")
elif (824 <= signo <= 923):
  print("virgo")
elif (924 <= signo <= 1023):
  print("libra")
elif (1024 <= signo <= 1122):
  print("escorpión")
elif (1123 <= signo <= 1222):
  print("sagitario")
elif (121 <= signo <= 219):
  print("acuario")
elif (220 <= signo <= 320):
  print("piscis")
else:
  print("capricornio")

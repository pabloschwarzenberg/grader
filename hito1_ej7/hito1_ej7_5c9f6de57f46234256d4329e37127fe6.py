#Zodiaco
Day=int(input("Ingrese día de nacimiento: "))
Mes=int(input("Ingrese mes de nacimiento: "))
if 31>=Day>=21 and Mes==3 or 1<=Day<=20 and Mes==4:
  print("aries")
elif 30>=Day>=21 and Mes==4 or 1<=Day<=21 and Mes==5:
  print("tauro")
elif 31>=Day>=22 and Mes==5 or 1<=Day<=21 and Mes==6:
  print("geminis")
elif 30>=Day>=22 and Mes==6 or 1<=Day<=22 and Mes==7:
  print("cancer")
elif 31>=Day>=23 and Mes==7 or 1<=Day<=22 and Mes==8:
  print("leo")
elif 30>=Day>=23 and Mes==8 or 1<=Day<=23 and Mes==9:
  print("virgo")
elif 30>=Day>=24 and Mes==9 or 1<=Day<=23 and Mes==10:
  print("libra")
elif 31>=Day>=24 and Mes==10 or 1<=Day<=22 and Mes==11:
  print("escorpio")
elif 30>=Day>=23 and Mes==11 or 1<=Day<=21 and Mes==12:
  print("sagitario")
elif 31>=Day>=22 and Mes==12 or 1<=Day<=21 and Mes==1:
  print("capricornio")
elif 31>=Day>=22 and Mes==1 or 1<=Day<=19 and Mes==2:
  print("acuario")
elif 28>=Day>=20 and Mes==2 or 1<=Day<=20 and Mes==3:
  print("piscis")
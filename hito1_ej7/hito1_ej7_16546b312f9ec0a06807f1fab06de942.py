#Zodiaco
d=int(input("ingrese el dia de su nacimiento: "))
m=int(input("ingrese el numero de su mes de nacimiento: "))
if((m==3 and d>=21) or (m==4 and d<=20)):
  print("aries")
if((m==4 and d>=21) or (m==5 and d<=20)):
  print("tauro")
if((m==5 and d>=21) or (m==6 and d<=21)):
  print("geminis")
if((m==6 and d>=22) or (m==7 and d<=22)):
  print("cancer")
if((m==7 and d>=23) or (m==8 and d<=22)):
  print("leo")
if((m==8 and d>=23) or (m==9 and d<=22)):
  print("virgo")
if((m==9 and d>=23) or (m==10 and d<=22)):
  print("libra")
if((m==10 and d>=23) or (m==11 and d<=22)):
  print("escorpion")
if((m==11 and d>=23) or (m==12 and d<=21)):
  print("sagitario")
if((m==12 and d>=21) or (m==1 and d<=20)):
  print("capricornio")
if((m==1 and d>=21) or (m==2 and d<=18)):
  print("acuario")
if((m==2 and d>=19) or (m==3 and d<=20)):
  print("piscis")     
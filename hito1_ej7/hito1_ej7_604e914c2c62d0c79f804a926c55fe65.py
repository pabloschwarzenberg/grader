#Zodiaco
d=int(input("Ingrese día:"))
m=int(input("Ingrese mes:"))
if ((m==3 and d>21) or (m==4 and d<=20)):
  print("Aries")
elif ((m==4 and d>=21) or (m==5 and d<=21)):
  print("Tauro")
elif ((m==5 and d>=22) or (m==6 and d<=21)):
 print("Geminis")
elif ((m==6 and d>=22) or (m==7 and d<=22)):
  print("Cancer")
elif ((m==7 and d>=23) or (m==8 and d<=22)):
  print("Leo")
elif ((m==8 and d>=23) or (m==9 and d<=23)):
  print("Virgo")
elif ((m==9 and d>=24) or (m==10 and d<=23)):
  print("Libra")
elif ((m==10 and d>=24) or (m==11 and d<=22)):
  print("Escorpio")
elif ((m==11 and d>=23) or (m==12 and d<=21)):
  print("Sagitario")
elif ((m==12 and d>=22) or (m==1 and d<=20)):
  print("Capricornio")
elif ((m==1 and d>=21) or (m==2 and d<=19)):
  print("Acuario")
elif ((m==2 and d>=20) or (m==3 and d<=20)):
  print("Piscis")
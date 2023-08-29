#Zodiaco
d=int(input())
m=int(input())
if m==3 and 21<=d or m==4 and d<=20:
  print("Aries")
elif m==4 and 21<=d or m==5 and d<=21:
  print("Tauro")
elif m==5 and 22<=d or m==6 and d<=21:
  print("Geminis")
elif m==6 and 22<=d or m==7 and d<=22:
  print("Cancer")
elif m==7 and 23<=d or m==8 and d<=22:
  print("Leo")
elif m==8 and 23<=d or m==9 and d<=23:
  print("Virgo")
elif m==9 and 24<=d or m==10 and d<=23:
  print("Libra")
elif m==10 and 24<=d or m==11 and d<=22:
  print("Escorpión")
elif m==11 and 23<=d or m==12 and d<=21:
  print("Sagitario")
elif m==12 and 22<=d or m==1 and d<=20:
  print("Capricornio")
elif m==1 and 21<=d or m==2 and d<=19:
  print("Acuario")
elif m==2 and 20<=d or m==3 and d<=20:
  print("Piscis")
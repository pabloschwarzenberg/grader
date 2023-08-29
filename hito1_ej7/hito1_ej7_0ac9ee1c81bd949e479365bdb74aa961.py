#Zodiaco
d=eval(input())
m=eval(input())
if  (21<=d<=31 and m==3) or (1<=d<=20 and m==4):
  print("Aries")
elif  (21<=d<=30 and m==4) or (1<=d<=21 and m==5):
  print("Tauro")
elif  (22<=d<=31 and m==5) or (1<=d<=21 and m==6):
  print("Geminis")
elif  (22<=d<=30 and m==6) or (1<=d<=22 and m==7):
  print("Cancer")
elif  (23<=d<=31 and m==7) or (1<=d<=22 and m==8):
  print("Leo")
elif  (23<=d<=31 and m==8) or (1<=d<=23 and m==9):
  print("Virgo")
elif  (24<=d<=30 and m==9) or (1<=d<=23 and m==10):
  print("Libra")
elif  (24<=d<=31 and m==10) or (1<=d<=22 and m==11):
  print("Escorpio")
elif  (23<=d<=30 and m==11) or (1<=d<=21 and m==12):
  print("Sagitario")
elif  (22<=d<=31 and m==12) or (1<=d<=20 and m==1):
  print("Capricornio")
elif  (21<=d<=31 and m==1) or (1<=d<=19 and m==2):
  print("Acuario")
elif  (20<=d<=28 and m==2) or (1<=d<=20 and m==3):
  print("Piscis")
else:
  print("LA FECHA INGRESADA NO ES VALIDA")
#Zodiaco
d=int(input("¿cual es tu día de nacimiento? "))
m=int(input("¿en cual mes naciste?(en formato del 1 al 12) "))
if (d>=22 and m==3 or d<=20 and m==4):
  print("tu signo zodiacal es Aries")
elif (d>=21 and m==4 or d<=22 and m==5):
  print("tu signo zodiacal es Tauro")
elif (d>=23 and m==5 or d<=21 and m==5):
  print("tu signo Zodiacal es geminis")
elif (d>=22 and m==6 or d<=23 and m==7):
  print("tu signo Zodiacal es Cancer")
elif (d>=24 and m==7 or d<=23 and m==8):
  print("tu signo Zodiacal es Leo")
elif (d>=23 and m==8 or d<=22 and m==9):
  print("tu signo Zodiacal es Virgo")
elif (d>=23 and m==9 or d<=22 and m==10):
  print("tu signo Zodiacal es Libra")
elif (d>=23 and m==10 or d<=22 and m==11):
  print("tu signo Zodiacal es Escorpio")
elif (d>=23 and m==11 or d<=22 and m==12):
  print("tu signo Zodiacal es Sagitario")
elif(d>=23 and m==12 or d<=20 and m==1):
  print("tu signo Zodiacal es Capricornio")
elif(d>=21 and m==1 or d<=18 and m==2):
  print("tu signo Zodiacal es Acuario")
elif(d>=19 and m==2 or d<=21 and m==3):
  print("tu signo Zodiacal es Piscis")
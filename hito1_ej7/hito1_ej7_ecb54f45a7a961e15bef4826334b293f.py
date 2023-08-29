#Zodiaco
#enero(31)[1] febrero(28)[2] marzo(31)[3] abril(30)[4] mayo(31)[5] junio(30)[6] julio(31)[7] 
#agosto(31)[8] septiembre(30)[9] octubre(31)[10] noviembre(30)[11] diciembre(31)[12]
a=int(input())
b=int(input())
if (a>=21 and a<=31 and b==3) or (a>=1 and a<=20 and b==4):
   print("aries")
elif (a>=21 and a<=30 and b==4) or (a>=1 and a<=21 and b==5): 
   print("tauro")
elif (a>=22 and a<=31 and b==5) or (a>=1 and a<=21 and b==6):
   print("geminis")
elif (a>=22 and a<=30 and b==6) or (a>=1 and a<=22 and b==7):
   print("cancer")
elif (a>=23 and a<=31 and b==7) or (a>=1 and a<=22 and b==8):
   print("leo")
elif (a>=23 and a<=31 and b==8) or (a>=1 and a<=23 and b==9):
   print("virgo")
elif (a>=24 and a<=30 and b==9) or (a>=1 and a<=23 and b==10):
   print("libra")
elif (a>=24 and a<=31 and b==10) or (a>=1 and a<=22 and b==11):
   print("escorpion")
elif (a>=23 and a<=30 and b==11) or (a>=1 and a<=21 and b==12):
   print("sagitario")
elif (a>=22 and a<=31 and b==12) or (a>=1 and a<=20 and b==1):
   print("capricornio")
elif (a>=21 and a<=31 and b==1) or (a>=1 and a<=19 and b==2):
   print("aquario")
elif (a>=20 and a<=28 and b==2) or (a>=1 and a<=20 and b==3):
   print("piscis")
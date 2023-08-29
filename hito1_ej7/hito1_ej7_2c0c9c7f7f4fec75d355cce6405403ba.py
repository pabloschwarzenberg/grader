#Zodiaco
d=int(input())
m=int(input())
if (d>=22 and m==12) or (d<=20 and m==1):
  s="Capricornio"
elif (d>=21 and m==1) or (d<=19 and m==2):
  s="Acuario"
elif (d>=20 and m==2) or (d<=20 and m==3):
  s="Piscis"
elif (d>=21 and m==3) or (d<=20 and m==4):
  s="Aries"
elif (d>=21 and m==4) or (d<=21 and m==5):
  s="Tauro"
elif (d>=22 and m==5) or (d<=21 and m==6):
  s="Geminis"
elif (d>=22 and m==6) or (d<=22 and m==7):
  s="Cancer"
elif (d>=23 and m==7) or (d<=22 and m==8):
  s="Leo"
elif (d>=23 and m==8) or (d<=23 and m==9):
  s="Virgo"
elif (d>=24 and m==9) or (d<=23 and m==10):
  s="Libra"
elif (d>=24 and m==10) or (d<=22 and m==11):
  s="Escorpion"
elif (d>=23 and m==11) or (d<=21 and m==12):
  s="Sagitario"  
print(s)
print("Ingrese su fecha de cumpleaños")
d=int(input("Día: "))
m=int(input("Mes: "))
if (d>=21 and m==3) or (d<=20 and m==4):
  s="aries"
elif (d>=21 and m==4) or (d<=21 and m==5):
  s="tauro"
elif (d>=22 and m==5) or (d<=21 and m==6):
  s="gemini"
elif (d>=22 and m==6) or (d<=22 and m==7):
  s="cáncer"
elif (d>=23 and m==7) or (d<=22 and m==8):
  s="leo"
elif (d>=23 and m==8) or (d<=23 and m==9):
  s="virgo"
elif (d>=24 and m==9) or (d<=23 and m==10):
  s="libra"
elif (d>=24 and m==10) or (d<=22 and m==11):
  s="escorpio"
elif (d>=23 and m==11) or (d<=21 and m==12):
  s="sagitario"
elif (d>=22 and m==12) or (d<=20 and m==1):
  s="capricornio"
elif (d>=21 and m==1) or (d<=19 and m==2):
  s="acuario"
elif (d>=20 and m==2) or (d<=20 and m==3):
  s="piscis"
print(s)
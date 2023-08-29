#Zodiaco
D=int(input("inserte día:"))
M=int(input("inserte mes:"))
if (bool(M==12))==True:
  if (bool(D<=21))==True:
    print("Sagitario")
  else:
    print("Capricornio")
elif (bool(M==1))==True:
  if (bool(D<=20))==True:
    print("Capricornio")
  else:
    print("Aquario")
elif (bool(M==2))==True:
  if (bool(D<=19))==True:
    print("Aquario")
  else:
    print("Picis")
elif (bool(M==3))==True:
  if (bool(D<=20))==True:
    print("Picis")
  else:
    print("Aries")
elif (bool(M==4))==True:
  if (bool(D<=20))==True:
    print("Aries")
  else:
    print("Tauro")
elif (bool(M==5))==True:
  if (bool(D<=21))==True:
    print("Tauro")
  else:
    print("Gemini")
elif (bool(M==6))==True:
  if (bool(D<=21))==True:
    print("Gemini")
  else:
    print("Cancer")
elif (bool(M==7))==True:
  if (bool(D<=22))==True:
    print("Cancer")
  else:
    print("Leo")
elif (bool(M==8))==True:
  if (bool(D<=22))==True:
    print("Leo")
  else:
    print("Virgo")
elif (bool(M==9))==True:
  if (bool(D<=23))==True:
    print("Virgo")
  else:
    print("Libra")
elif (bool(M==10))==True:
  if (bool(D<=23))==True:
    print("Libra")
  else:
    print("Scorpio")
elif (bool(M==11))==True:
  if (bool(D<=22))==True:
    print("Scorpio")
  else:
    print("Sagitario")
else:
  print("Sagitario")
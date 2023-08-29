n=int(input("Ingrese un dia: "))
m=int(input("Ingrese un mes: "))
if m==1:
  if 1<=n<=19:
    print("Capricornio")
  elif 20<=n<=31:
    print("Acuario")
elif m==2:
  if 1<=n<=19:
    print("Acuario")
  elif 20<=n<=28:
    print("Piscis")
elif m==3:
  if 21<=n<=31:
    print("Aries")
  elif 1<=n<=20:
    print("Piscis")
elif m==4:
  if 1<=n<=20:
    print("Aries")
  elif 21<=n<=30:
    print("Tauro")
elif m==5:
  if 1<=n<=20:
    print("Tauro")
  elif 21<=n<=31:
    print("Geminis")
elif m==6:
  if 1<=n<=21:
    print("Geminis")
  elif 22<=n<=30:
    print("Cancer")
elif m==7:
  if 1<=n<=22:
    print("Cancer")
  elif 23<=n<=31:
    print("Leo")
elif m==8:
  if 1<=n<=23:
    print("Leo")
  elif 24<=n<=31:
    print("Virgo")
elif m==9:
  if 1<=n<=23:
    print("Virgo")
  elif 24<=n<=30:
    print("Libra")
elif m==10:
  if 1<=n<=22:
    print("Libra")
  elif 23<=n<=31:
    print("Escorpion")
elif m==11:
  if 1<=n<=22:
    print("Escorpion")
  elif 23<=n<=30:
    print("Sagitario")
elif m==12:
  if 1<=n<=21:
    print("Sagitario")
  elif 22<=n<=31:
    print("Capricornio")

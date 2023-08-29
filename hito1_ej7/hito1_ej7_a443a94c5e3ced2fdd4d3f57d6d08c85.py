#Zodiaco
dia= int(input("ingrese el dia de su cumpleaños: "))
mes= int(input("ingrese el mes de su cumpleaños: "))
if mes==1:
  print("enero")
  if 1<=dia<=20:
    print("Capricornio")
  elif 21<=dia<=30:
    print("Acuario")
elif mes==2:
  print("febrero")
  if 1<=dia<=19:
    print("Acuario")
  elif 20<=dia<=28:
    print("Piscis") 
elif mes==3:
  print("marzo")
  if 1<=dia<=20:
    print("Piscis")
  elif 21<=dia<=31:
    print("Aries")
elif mes==4:
  print("abril")
  if 1<=dia<=19:
    print("Aries") 
  elif 20<=dia<=30:
    print("Tauro")
elif mes==5:
  print("mayo")
  if 1<=dia<=20:
    print("Tauro")
  elif 21<=dia<=29:
    print("Geminis")
elif mes==6:
  print("junio")
  if 1<=dia<=20:
    print("Gemenis")
  elif 21<=dia<=30:
    print("Cancer")
elif mes==7:
  print("julio")
  if 1<=dia<=22:
    print("Cancer")
  elif 23<=dia<=31:
    print("Leo")
elif mes==8:
  print("agosto")
  if 1<=dia<=22:
    print("Leo")
  elif 23<=dia<=31:
    print("Virgo")
elif mes==9:
  print("septiembre")
  if 1<=dia<=22:
    print("Virgo")
  elif 23<=dia<=30:
    print("Libra")
elif mes==10:
  print("octubre")
  if 1<=dia<=22:
    print("Libra")
  elif 23<=dia<=31:
    print("Escorpio")
elif mes==11:
  print("noviembre")
  if 1<=dia<=21:
    print("Escorpio")
  elif 22<=dia<=30:
    print("Sagitario")
elif mes==12:
  print("diciembre")
  if 1<=dia<=21:
    print("Sagitario")
  elif 22<=dia<=31:
    print("Capricornio")
else:
    print("datos invalidos...")
#Zodiaco
dia=int(input("Ingrese el día de su cumpleaños: "))
mes=int(input("Ingrese el mes de su cumpleaños: "))

if mes==4 and 20<=dia<=30:
  print("tauro")
elif mes==5 and 1<=dia<21:
  print("tauro")
elif mes==5 and 21<=dia<=31:
  print("geminis")
elif mes==6 and 1<=dia<21:
  print("geminis")
elif mes==6 and 21<=dia<=30:
  print("cancer")
elif mes==7 and 1<=dia<23:
  print("cancer")
elif mes==7 and 23<=dia<=31:
  print("leo")
elif mes==8 and 1<=dia<23:
  print("leo")
elif mes==8 and 23<=dia<31:
  print("virgo")
elif mes==9 and 1<=dia<23:
  print("virgo")
elif mes==9 and 23<=dia<=30:
  print("libra")
elif mes==10 and 1<=dia<23:
  print("libra")
elif mes==10 and 23<=dia<=31:
  print("escorpio")
elif mes==11 and 1<=dia<=22:
  print("escorpio")
elif mes==11 and 23<=dia<=30:
  print("sagitario")
elif mes==12 and 1<=dia<=22:
  print("sagitario")
elif mes==12 and 23<=dia<=31:
  print("capricornio")
elif mes==1 and 1<=dia<=20:
  print("capricornio")
elif mes==1 and 21<=dia<=31:
  print("acuario")
elif mes==2 and 1<=dia<=19:
  print("acuario")
elif mes==2 and 20<=dia<=28:
  print("piscis")
elif mes==3 and 1<=dia<=21:
  print("piscis")
elif mes==3 and 22<=dia<=31:
  print("aries")
else:
  print("aries")



#Signo del Zodíaco.
Dia=int(input("Ingrese el dia de nacimiento:"))
Mes=int(input("Ingrese el mes de nacimiento en número:"))
if Mes==1 and 20<=Dia<=31 or Mes==2 and 1<=Dia<=19:
  print("Acuario")
elif Mes==2 and 20<=Dia<=28 or Mes==3 and 1<=Dia<=21:
  print("Piscis")
elif Mes==3 and 22<=Dia<=31 or Mes==4 and 1<=Dia<=20:
  print("Aries")
elif Mes==4 and 21<=Dia<=30 or Mes==5 and 1<=Dia<=21:
  print("Tauro")
elif Mes==5 and 22<=Dia<=31 or Mes==6 and 1<=Dia<=21:
  print("Geminis")
elif Mes==6 and 22<=Dia<=30 or Mes==7 and 1<=Dia<=23:
  print("Cancer")
elif Mes==7 and 24<=Dia<=31 or Mes==8 and 1<=Dia<=23:
  print("Leo")
elif Mes==8 and 24<=Dia<=31 or Mes==9 and 1<=Dia<=23:
  print("Virgo")
elif Mes==9 and 24<=Dia<=30 or Mes==10 and 1<=Dia<=23:
  print("Libra")
elif Mes==10 and 24<=Dia<=31 or Mes==11 and 1<=Dia<=22:
  print("Escorpio")
elif Mes==11 and 23<=Dia<=30 or Mes==12 and 1<=Dia<=22:
  print("Sagitario")
elif Mes==12 and 23<=Dia<=31 or Mes==1 and 1<=Dia<=19:
  print("Capricornio")     
#Zodiaco
Dia=int(input("Ingrese su dia de nacimiento:"))
Mes=int(input("Ingrese su mes de nacimiento en número:"))
print("Su dia de nacimiento y mes de nacimiento es:{Dia},{Mes}")
if Mes==1 and 20<=Dia<=31 or Mes==2 and 1<=Dia<=19:
  print("Su signo es Acuario")
elif Mes==2 and 20<=Dia<=28 or Mes==3 and 1<=Dia<=21:
  print("Su signo es Piscis")
elif Mes==3 and 22<=Dia<=31 or Mes==4 and 1<=Dia<=20:
  print("Su singno es Aries")
elif Mes==4 and 21<=Dia<=30 or Mes==5 and 1<=Dia<=21:
  print("Su signo es Tauro")
elif Mes==5 and 22<=Dia<=31 or Mes==6 and 1<=Dia<=21:
  print("Su signo es Geminis")
elif Mes==6 and 22<=Dia<=30 or Mes==7 and 1<=Dia<=23:
  print("Su signo es Cancer")
elif Mes==7 and 24<=Dia<=31 or Mes==8 and 1<=Dia<=23:
  print("Su signo es Leo")
elif Mes==8 and 24<=Dia<=31 or Mes==9 and 1<=Dia<=23:
  print("Su signo es Virgo")
elif Mes==9 and 24<=Dia<=30 or Mes==10 and 1<=Dia<=23:
  print("Su signo es Libra")
elif Mes==10 and 24<=Dia<=31 or Mes==11 and 1<=Dia<=22:
  print("Su signo es Escorpio")
elif Mes==11 and 23<=Dia<=30 or Mes==12 and 1<=Dia<=22:
  print("Su singo es Sagitario")
elif Mes==12 and 23<=Dia<=31 or Mes==1 and 1<=Dia<=19:
  print("Su singo es Capricornio")
      
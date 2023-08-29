#Zodiaco
Dia=int(input("Ingrese su día de nacimiento:"))
Mes=int(input("Ingrese su mes de nacimiento en numero:"))
print(f"Su día y mes de nacimiento es: {Dia}, {Mes}")
if Mes==1 and 21<=Dia<=31 or Mes==2 and 1<=Dia<=19:
  print("Su Signo es ACUARIO")
elif Mes==2 and 20<=Dia<=28 or Mes==3 and 1<=Dia<=21:
  print("Su Signo es PISCIS")
elif Mes==3 and 22<=Dia<=31 or Mes==4 and 1<=Dia<=20:
  print("Su Signo es ARIES")
elif Mes==4 and 21<=Dia<=30 or Mes==5 and 1<=Dia<=21:
  print("Su signo es TAURO")
elif Mes==5 and 22<=Dia<=31 or Mes==6 and 1<=Dia<=21:
  print("Su Signo es GEMINIS")
elif Mes==6 and 22<=Dia<=30 or Mes==7 and 1<=Dia<=23:
  print("Su Signo es CANCER")
elif Mes==7 and 24<=Dia<=31 or Mes==8 and 1<=Dia<=23:
  print("Su signo es LEO")
elif Mes==8 and 24<=Dia<=31 or Mes==9 and 1<=Dia<=23:
  print("Su Signo es VIRGO")
elif Mes==9 and 24<=Dia<=30 or Mes==10 and 1<=Dia<=23:
  print("Su Signo es LIBRA")
elif Mes==10 and 24<=Dia<=31 or Mes==11 and 1<=Dia<=22:
  print("Su signo es ESCORPIO")
elif Mes==11 and 23<=Dia<=30 or Mes==12 and 1<=Dia<=22:
  print("Su Signo es SAGITARIO")
else:
  Mes==12 and 23<=Dia<=31 or Mes==1 and 1<=Dia<=20
  print("Su Signo es CAPRICORNIO")
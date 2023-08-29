#Zodiaco
dia = int(input('Ingrese su dia de nacimiento: '))
mes = int(input('Ingrese su mes nacimiento: '))

Fecha = int(str(mes)+str(dia).zfill(2))

Lista = [11, 120, 219, 321, 420, 521, 621, 723, 823, 923, 1023, 1123, 1222, 1231]

if (Fecha >= Lista[0]) and (Fecha <= Lista[1]):
   print("Su signo es: Capricornio")

if (Fecha > Lista[1]) and (Fecha <= Lista[2]):
   print("Su signo es: Acuario")

if (Fecha > Lista[2]) and (Fecha <= Lista[3]):
   print("Su signo es: Piscis")   

if (Fecha > Lista[3]) and (Fecha <= Lista[4]):
   print("Su signo es: Aries")   

if (Fecha > Lista[4]) and (Fecha <= Lista[5]):
   print("Su signo es: Tauro")   

if (Fecha > Lista[5]) and (Fecha <= Lista[6]):
   print("Su signo es: Geminis")

if (Fecha > Lista[6]) and (Fecha <= Lista[7]):
   print("Su signo es: Cancer")

if (Fecha > Lista[7]) and (Fecha <= Lista[8]):
   print("Su signo es: Leo")

if (Fecha > Lista[8]) and (Fecha <= Lista[9]):
   print("Su signo es: Virgo")

if (Fecha > Lista[9]) and (Fecha <= Lista[10]):
   print("Su signo es: Libra")

if (Fecha > Lista[10]) and (Fecha <= Lista[11]):
   print("Su signo es: Escorpion")

if (Fecha > Lista[11]) and (Fecha <= Lista[12]):
   print("Su signo es: Sagitario")

if (Fecha > Lista[12]) and (Fecha <= Lista[13]):
   print("Su signo es: Capricornio")


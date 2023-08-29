#Zodiaco
D = int(input("Introducir día de cumpleaños:"))
M = int(input("Introducir mes de cumpleaños (en números):"))
if (D>=21 and M==3) or (D<=20 and M==4):
  print("Su signo del Zodiaco es Aries")
if (D>=21 and M==4) or (D<=21 and M==5):
  print("Su signo del Zodiaco es Tauro")
if (D>=22 and M==5) or (D<=21 and M==6):
  print("Su signo del Zodiaco es Géminis")
if (D>=22 and M==6) or (D<=22 and M==7):
  print("Su signo del Zodiaco es Cáncer")
if (D>=23 and M==7) or (D<=22 and M==8):
  print("Su signo del Zodiaco es Leo")
if (D>=23 and M==8) or (D<=23 and M==9):
  print("Su signo del Zodiaco es Virgo")
if (D>=24 and M==9) or (D<=23 and M==10):
  print("Su signo del Zodiaco es Libra")
if (D>=24 and M==10) or (D<=22 and M==11):
  print("Su signo del Zodiaco es Escorpión")
if (D>=23 and M==11) or (D<=21 and M==12):
  print("Su signo del Zodiaco es Sagitario")
if (D>=22 and M==12) or (D<=20 and M==1):
  print("Su signo del Zodiaco es Capricornio")
if (D>=21 and M==1) or (D<=19 and M==2):
  print("Su signo del Zodiaco es Acuario")
if (D>=20 and M==2) or (D<=20 and M==3):
  print("Su signo del Zodiaco es Piscis")
else:
  print("ERROR: try again")
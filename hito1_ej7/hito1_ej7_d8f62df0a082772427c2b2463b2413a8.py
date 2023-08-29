#Signos Zodiacales
print("Ingrese la fecha de su nacimiento para saber qué signo zodiacal es usted.")
dia = int(input("Ingrese el valor de dia: "))
mes = int(input("Ingrese el valor de mes: "))

if (dia >=22 and mes == 12) or (dia <=20 and mes == 1):
  print("capricornio.")
elif (dia >=21 and mes == 1) or (dia <=19 and mes == 2):
  print("acuario.")
elif (dia >=20 and mes == 2) or (dia <=20 and mes == 3):
  print("piscis.")
elif (dia >=21 and mes == 3) or (dia <=20 and mes == 4):
  print("aries.")
elif (dia >=21 and mes == 4) or (dia <=21 and mes == 5):
  print("tauro.")
elif (dia >=22 and mes == 5) or (dia <=21 and mes == 6):
  print("géminis.")
elif (dia >=21 and mes == 6) or (dia <=23 and mes == 7):
  print("cancer.")
elif (dia >=24 and mes == 7) or (dia <=23 and mes == 8):
  print("leo.")
elif (dia >=24 and mes == 8) or (dia <=23 and mes == 9):
  print("virgo.")
elif (dia >=24 and mes == 9) or (dia <=23 and mes == 10):
  print("libra.")
elif (dia >=24 and mes == 10) or (dia <=22 and mes == 11):
  print("escorpio.")
elif (dia >=23 and mes == 11) or (dia <=21 and mes == 12):
  print("sagitario.")
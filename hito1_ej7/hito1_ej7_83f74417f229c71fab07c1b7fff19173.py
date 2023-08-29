#Para determinar las fechas de cada signo utiliza la columna Tropical Zodiac en la tabla de fechas que aparece en este link (Wikipedia).
#Códigos:
#Signo del Zodíaco

print("***Signo del zodiaco a partir de su fecha de cumpleaños***")
while True:
  dia=int(input("Ingrese el día: "))
  if(dia>31 or dia<1):
    print("Día inválido, vuelva a intentarlo")
  else:
    break
while True:
  mes=int(input("Ingrese el mes: "))
  if(mes>12 or mes<1):
    print("Mes inválido, vuelva a intentarlo")
  else:
    break

if(mes>=1 and mes<=12):
  if(mes==3 and dia>=21):
    print("Usted es Aries")
  elif(mes==4 and dia<=20):
    print("Usted es Aries")
  elif(mes==4 and dia>=21):
    print("Usted es Tauro")
  elif(mes==5 and dia<=20):
    print("Usted es Tauro")
  if(mes==5 and dia>=21):
    print("Usted es Géminis")
  if(mes==6 and dia<=21):
    print("Usted es Géminis")
  if(mes==6 and dia>=22):
    print("Usted es cancer")
  if(mes==7 and dia<=22):
    print("Usted es cancer")
  if(mes==7 and dia>=23):
    print("Usted es Leo")
  if(mes==8 and dia<=22):
    print("Usted es Leo")
  if(mes==8 and dia>=23):
    print("Usted es Virgo")
  if(mes==9 and dia<=22):
    print("Usted es Virgo")
  if(mes==9 and dia>=23):
    print("Usted es Libra")
  if(mes==10 and dia<=22):
    print("Usted es Libra")
  if(mes==10 and dia>=23):
    print("Usted es Escorpio")
  if(mes==11 and dia<=22):
    print("Usted es Escorpio")
  if(mes==11 and dia>=23):
    print("Usted es Sagitario")
  if(mes==12 and dia<=21):
    print("Usted es Sagitario")
  if(mes==12 and dia>=22):
    print("Usted es Capricornio")
  if(mes==1 and dia<=20):
    print("Usted es Capricornio")
  if(mes==1 and dia>=21):
    print("Usted es Acuario")
  if(mes==2 and dia<=18):
    print("Usted es Acuario")
  if(mes==2 and dia>=19):
    print("Usted es Piscis")
  if(mes==3 and dia<=20):
    print("Usted es Piscis")
      
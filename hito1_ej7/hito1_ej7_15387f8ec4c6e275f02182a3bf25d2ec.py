#Zodiaco
#signo del zodiaco
#ENERO = 1
#FEBRER0 = 2
#MARZO = 3
#ABRIL = 4
#MAYO = 5
#JUNIO = 6
#JULIO = 7
#AGOSTO = 8
#SEPTIEMBRE = 9
#OCTUBRE = 10
#NOVIEMBRE = 11
#DICIEMBRE = 12
print("Sacar el signo del zodiaco")
dia = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))
if dia >= 21 and mes == 3 or dia <=20 and mes==4:
  print("aries")
if dia >= 21 and mes == 4 or dia <=20 and mes==5:
  print("tauro")
if dia >= 21 and mes == 5 or dia <=21 and mes==6:
  print("geminis")
if dia >= 22 and mes == 6 or dia <=21 and mes==7:
  print("cancer")
if dia >= 22 and mes == 7 or dia <=23 and mes==8:
  print("leo")
if dia >= 24 and mes == 8 or dia <=23 and mes==9:
  print("virgo")
if dia >= 24 and mes == 9 or dia <=22 and mes==10:
  print("libra")
if dia >= 23 and mes == 10 or dia <=22 and mes==11:
  print("escorpio")
if dia >= 23 and mes == 11 or dia <=21 and mes==12:
  print("sagitario")
if dia >= 22 and mes == 12 or dia <=20 and mes==1:
  print("capricornio")
if dia >= 21 and mes == 1 or dia <=19 and mes==2:
  print("acuario")
if dia >= 20 and mes == 2 or dia <=20 and mes==3:
  print("piscis")
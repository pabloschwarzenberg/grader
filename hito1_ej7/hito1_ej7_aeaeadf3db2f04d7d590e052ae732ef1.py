#Zodiaco
dia = int(input("Introduce el dia de tu nacimiento: "))
mes = int(input("Introduce el mes de tu nacimiento: "))

if mes > 12 or mes < 0 and dia > 32 or dia < 0:
  print("INGRESE DATOS VALIDOS")
if mes == 1 and dia in range(20,31) or mes == 2 and dia in range(1,19):
  print("Acuario")
if mes == 2 and dia in range(19,28) or mes == 3 and dia in range(1,21):
  print("Piscis")
if mes == 3 and dia in range(21,31) or mes == 4 and dia in range(1,20):
  print("Aries")
if mes == 4 and dia in range(20,30) or mes == 5 and dia in range(1,21):
  print("Tauro")
if mes == 5 and dia in range(21,31) or mes == 6 and dia in range(1,21):
  print("Geminis")
if mes == 6 and dia in range(21,30) or mes == 7 and dia in range(1,23):
  print("Cancer")
if mes == 7 and dia in range(23,31) or mes == 8 and dia in range(1,23):
  print("Leo")
if mes == 8 and dia in range(23,31) or mes == 9 and dia in range(1,23):
  print("Virgo")
if mes == 9 and dia in range(23,30) or mes == 10 and dia in range(1,23):
  print("Libra")
if mes == 10 and dia in range(23,31) or mes == 11 and dia in range(1,22):
  print("Escorpio")
if mes == 11 and dia in range(22,30) or mes == 12 and dia in range(1,22):
  print("Sagitario")
if mes == 12 and dia in range(22,31) or mes == 1 and dia in range(1,20):
  print("Capricornio")

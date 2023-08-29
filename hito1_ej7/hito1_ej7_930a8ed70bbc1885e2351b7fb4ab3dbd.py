#Zodiaco
##Escribe un programa que reciba como parámetro el día y el mes del cumpleaños de una persona (como números enteros) y que imprima el signo del zodíaco al que pertenece.
##Entrada de datos 
dia = int(input("Ingrese el dia de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento: "))
print("------------------------------------------")
if mes == 3 and dia >= 21: 
 print("Su signo zodiacal es ARIES")
  
elif mes == 4 and dia <= 20:
 print("Su signo zodiacal es ARIES")
  
elif mes == 4 and dia >= 21:
 print("Su signo zodiacal es TAURO")
  
elif mes == 5 and dia <= 20:
 print("Su signo zodiacal es TAURO") 
  
elif mes == 5 and dia >= 21:
 print("Su signo zodiacal es GEMINIS")

elif mes == 6 and dia <= 21:
 print("Su signo zodiacal es GEMINIS") 

elif mes == 6 and dia >= 22:
 print("Su signo zodiacal es CANCER") 

elif mes == 7 and dia <= 21:
 print("Su signo zodiacal es CANCER") 

elif mes == 7 and dia >= 22:
  print("Su signo zodiacal es LEO")

elif mes == 8 and dia <= 23:
  print("Su signo zodiacal es LEO")

elif mes == 8 and dia >= 24:
  print("Su signo zodiacal es VIRGO")
  
elif mes == 9 and dia <= 23:
  print("Su signo zodiacal es VIRGO")

elif mes == 9 and dia >= 24:
  print("Su signo zodiacal es LIBRA")

elif mes == 10 and dia <= 22:
  print("Su signo zodiacal es LIBRA")

elif mes == 11 and dia >= 23:
  print("Su signo zodiacal es ESCORPIO")

elif mes == 11 and dia <= 22:
  print("Su signo zodiacal es ESCORPIO")

elif mes == 11 and dia >= 23:
  print("Su signo zodiacal es SAGITARIO")

elif mes == 12 and dia <= 21:
  print("Su signo zodiacal es SAGITARIO")

elif mes == 12 and dia >= 22:
  print("Su signo zodiacal es CAPRICORNIO")

elif mes == 1 and dia <= 20:
  print("Su signo zodiacal es CAPRICORNIO")

elif mes == 1 and dia >= 21:
  print("Su signo zodiacal es ACUARIO") 

elif mes == 2 and dia <= 19:
  print("Su signo zodiacal es ACUARIO")

elif mes == 2 and dia >= 20:
  print("Su signo zodiacal es PISCIS")

elif mes == 3 and dia <= 20:
  print("Su signo zodiacal es PISCIS") 
  
else:
  print("DATOS INCORRECTOS")
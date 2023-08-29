#Zodiaco
#zodiaco

dia = int(input("Ingresa tu día de nacimiento: "))
mes = int(input("Ingresa tu mes de nacimiento (del 1 al 12): "))


if (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
  resultado = "ARIES"
    
elif (dia >= 20 and mes == 4) or (dia <=21 and mes == 5):
  resultado = "TAURO"

elif (dia >= 21 and mes == 5) or (dia <= 21 and mes == 6):
  resultado = "GEMENIS"

elif (dia >= 21 and mes == 6) or (dia <= 23 and mes == 7):
  resultado = "CANCER"

elif (dia >= 23 and mes == 7) or (dia <= 23 and mes == 8):
  resultado = "LEO"

elif (dia >= 23 and mes == 8) or (dia <= 23 and mes == 9):
  resultado = "VIRGO"
    
elif (dia >= 23 and mes == 9) or (dia <= 23 and mes == 10):
  resultado = "LIBRA"
    
elif (dia >= 23 and mes == 10) or (dia <= 22 and mes == 11):
  resultado = "ESCORPIÓN"

elif (dia >= 23 and mes == 11) or (dia <= 22 and mes == 12):
  resultado = "SAGITARIO"

elif (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
  resultado = "CAPRICORNIO"
    
elif (dia >= 20 and mes == 1) or (dia <= 19 and mes == 2):
  resultado = "ACUARIO"

else:
  resultado = "PISCIS"


print("Tu signo zodiacal es: ", resultado)
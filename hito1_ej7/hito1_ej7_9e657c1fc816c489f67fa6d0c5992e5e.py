#Zodiaco
dia = int(input())
mes = int(input())

zod = ' '
pisis   = (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20)

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
  zod = "ARIES"

elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
  zod = "TAURO"

elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21):
  zod = "GEMINIS"

elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
  zod = "CANCER"

elif (mes == 3 and dia >= 23) or (mes == 8 and dia <= 23):
  zod = "LEO"

elif (mes == 8 and dia >= 24) or (mes == 9 and dia <= 22):
  zod = "VIRGO"
  
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 23):
  zod = "LIBRA"

elif (mes == 10 and dia >= 24) or (mes == 11 and dia <= 22):
  zod = "ESCORPION"
  
elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 22):
  zod = "SAGITARIO"
  
elif (mes == 12 and dia >= 23) or (mes == 1 and dia <= 20):
  zod = "CAPRICORNIO"
  
elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 18):
  zod = "ACUARIO"
 
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
  zod = "PICIS"

print(zod)
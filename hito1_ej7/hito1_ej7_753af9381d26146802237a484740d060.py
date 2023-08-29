#Zodiaco
dia = int(input("Ingrese su día de nacimiento: "))

while dia < 0 or dia >= 31:
  print("Dato inválido.")
  dia = int(input("Ingrese su día de nacimiento: "))

mes = int(input("ingrese su mes de nacimiento: "))

while mes < 0 or mes > 12:
  print("Dato inválido.")
  mes = int(input("Ingrese su mes de nacimiento: "))
#aries: 21 de marzo - 20 de abril
if (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
  print("ARIES")
#tauro: 21 de abril - 20 de mayo
elif (dia >= 21 and mes == 4) or (dia <= 20 and mes == 5):
  print("TAURO")
#geminis: 21 de mayo - 21 de junio
elif (dia >= 21 and mes == 5) or (dia <= 21 and mes == 6):
  print("GEMINIS") 

elif (dia >= 22 and mes == 6) or (dia <= 22 and mes == 7):
  print("CANCER")

elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
  print("LEO")  

elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
  print("VIRGO")

elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
  print("LIBRA")  

elif (dia >= 23 and mes == 10) or (dia <= 22 and mes == 11):
  print("ESCORPIO") 

elif (dia >= 23 and mes == 11) or (dia <= 21 and mes == 12):
  print("SAGITARIO")

elif (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
  print("CAPRICORNIO")  

elif (dia >= 21 and mes == 1) or (dia <= 18 and mes == 2):
  print("ACUARIO") 

elif(dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
  print("PISCIS")     
  
#Zodiaco

dia = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))
signo = ""

if((dia >=21 and mes == 3) or (dia <= 20 and mes == 4)):
  signo = "Aries"
elif((dia >=21 and mes == 4) or (dia <= 20 and mes == 5)):
  signo = "Tauro"
elif((dia >=21 and mes == 5) or (dia <= 20 and mes == 6)):
  signo = "Géminis"
elif((dia >=21 and mes == 6) or (dia <= 20 and mes == 7)):
  signo = "Cáncer"
elif((dia >=21 and mes == 7) or (dia <= 21 and mes == 8)):
  signo = "Leo"
elif((dia >=22 and mes == 8) or (dia <= 22 and mes == 9)):
  signo = "Virgo"
elif((dia >=23 and mes == 9) or (dia <= 22 and mes == 10)):
  signo = "Libra"
elif((dia >=23 and mes == 10) or (dia <= 22 and mes == 11)):
  signo = "Escorpio"
elif((dia >=23 and mes == 11) or (dia <= 20 and mes == 12)):
  signo = "Sagitario"
elif((dia >=21 and mes == 12) or (dia <= 19 and mes == 1)):
  signo = "Capricornio"
elif((dia >=20 and mes == 1) or (dia <= 18 and mes == 2)):
  signo = "Acuario"
elif((dia >=19 and mes == 2) or (dia <= 20 and mes == 3)):
  signo = "Picis"
  
print("Su signo es: ",signo)
#Zodiaco
dia = int(input("Ingres dia de Cumpleaños:"))
mes = int(input("Ingres mes de Cumpleaños:"))


if((dia >= 21 and mes == 3) or (dia <= 20 and mes == 4)):
    print("Aries")
if((dia >= 21 and mes == 4) or (dia < 21 and mes == 5)):
    print("Tauro")
if((dia >= 21 and mes == 5) or (dia < 20 and mes == 6)):
    print("geminis")
if((dia >= 21 and mes == 6) or (dia < 23 and mes == 7)):
    print("Cancer")
if((dia >= 23 and mes == 7) or (dia < 23 and mes == 8)):
    print("Leo")
if((dia >= 23 and mes == 8) or (dia < 23 and mes == 9)):
    print("Virgo")
if((dia >= 23 and mes == 9) or (dia < 23 and mes == 10)):
    print("Libra")
if((dia >= 23 and mes == 10) or (dia < 22 and mes == 11)):
    print("escorpio")
if((dia >= 23 and mes == 11) or (dia < 23 and mes == 12)):
    print("Sagitario")
if((dia >= 23 and mes == 12) or (dia < 20 and mes == 1)):
    print("Capricornio")
if((dia >= 20 and mes == 1) or (dia < 19 and mes == 2)):
    print("acuario")
if((dia >= 19 and mes == 2) or (dia < 21 and mes == 3)):
    print("Piscis")
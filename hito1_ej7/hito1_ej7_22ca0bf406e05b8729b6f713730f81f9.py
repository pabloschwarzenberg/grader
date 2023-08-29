#Zodiaco
dia = int(input("ingres dia de cumpleaños: "))
mes = int(input("ingres mes de cumpleaños: "))

if dia >= 21 and mes == 3 or dia <= 20 and mes == 4:
    print("Su signo zodiacal es Aries")
elif dia >= 21 and mes == 4 or dia <= 21 and mes == 5:
    print("Su signo zodiacal es Tauro")
elif dia >= 22 and mes == 5 or dia <= 21 and mes == 6:
    print("Su signo zodiacal es Geminis")
elif dia >= 22 and mes == 6 or dia <= 23 and mes == 7:
    print("Su signo zodiacal es Cancer")
elif dia >= 24 and mes == 7 or dia <= 23 and mes == 8:
    print("Su signo zodiacal es Leo")
elif dia >= 24 and mes == 8 or dia <= 23 and mes == 9:
    print("Su signo zodiacal es Virgo")
elif dia >= 24 and mes == 9 or dia <= 23 and mes == 10:
    print("Su signo zodiacal es Libra")
elif dia >= 24 and mes == 10 or dia <= 22 and mes == 11:
    print("Su signo zodiacal es Escorpion")
elif dia >= 23 and mes == 11 or dia <= 22 and mes == 12:
    print("Su signo zodiacal es Sagitario")
elif dia >= 23 and mes == 12 or dia <= 20 and mes == 1:
    print("Su signo zodiacal es Capricornio")
elif dia >= 21 and mes == 1 or dia <= 19 and mes == 2:
    print("Su signo zodiacal es Acuario")
else:
    if dia >= 2 and mes == 2 or dia <= 20 and mes == 3:
        print("Su signo zodiacal es Picis")
     
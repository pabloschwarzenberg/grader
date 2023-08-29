#Zodiaco
print("Por favor introduzca el dia y mes del cumpleaños de una persona como numeros enteros")
dia = int(input("Por favor introduzca el día: "))
mes = int(input("Por favor introduzca el mes: "))
if dia > 21 and mes == 3 or dia <= 20 and mes == 4:
    print("Signo zodiacal: Aries")
elif dia > 20 and mes == 4 or dia <= 21 and mes == 5:
    print("Signo zodiacal: Tauro")
elif dia > 21 and mes == 5 or dia <= 21 and mes == 6:
    print("Signo zodiacal: Geminis")
elif dia > 21 and mes == 6 or dia <= 23 and mes == 7:
    print("Signo zodiacal: Cancer")
elif dia > 23 and mes == 7 or dia <= 23 and mes == 8:
    print("Signo zodiacal: Leo")
elif dia > 23 and mes == 8 or dia <= 23 and mes == 9:
    print("Signo zodiacal: Virgo")
elif dia > 23 and mes == 9 or dia <= 23 and mes == 10:
    print("Signo zodiacal: Libra")
elif dia > 23 and mes == 10 or dia <= 22 and mes == 11:
    print("Signo zodiacal: Escorpio")
elif dia > 22 and mes == 11 or dia <= 22 and mes == 12:
    print("Signo zodiacal: Sagitario")
elif dia > 22 and mes == 12 or dia <= 20 and mes == 1:
    print("Signo zodiacal: Capricornio")
elif dia > 20 and mes == 1 or dia <= 19 and mes == 2:
    print("Signo zodiacal: Acuario")
elif dia > 19 and mes == 2 or dia <= 21 and mes == 3:
    print("Signo zodiacal: Piscis")
else:
    print("Fecha equivocada")
#Zodiaco
dia = int(input("Bienvenido, favor indicarme el día de su fecha de nacimiento:"))
mes = int(input("Mes de nacimiento:"))

if (dia > 21 and mes == 3) or (dia <= 20 and mes == 4):
    print("Tu signo del zodiaco es Aries")
elif (dia > 20 and mes == 4) or (dia <= 21 and mes == 5):
    print("Tu signo del zodiaco es Tauro")
elif (dia > 21 and mes == 5) or (dia <=21 and mes == 6):
    print("Tu signo del zodiaco es Geminis")
elif (dia > 21 and mes == 6) or (dia <= 23 and mes == 7):
    print("Tu signo del zodiaco es Cancer")
elif (dia > 23 and mes == 7) or (dia <= 23 and mes == 8):
    print("Tu signo del zodiaco es Leo")
elif (dia > 23 and mes == 8) or (dia <= 23 and mes == 9):
    print("Tu signo del zodiaco es Virgo")
elif (dia > 23 and mes == 9) or (dia <= 23 and mes == 10):
    print("Tu signo del zodiaco es Libra")
elif (dia > 23 and mes == 10) or (dia <= 22 and mes == 11):
    print("Tu signo del zodiaco es Scorpio")
elif (dia > 23 and mes == 11) or (dia <= 20 and mes == 12):
    print("Tu signo del zodiaco es Sagitario")
elif (dia > 2 and mes == 12) or (dia <= 22 and mes == 1):
    print("Tu signo del zodiaco es Capricornio")
elif (dia > 22 and mes == 1) or (dia <= 19 and mes == 2):
    print("Tu signo del zodiaco es Acuario")
elif (dia > 19 and mes == 2) or (dia <= 20 and mes == 3):
    print("Tu signo del zodiaco es Piscis")
#Zodiaco

dia = eval(input("Ingrese día de nacimiento (en números): "))
mes = eval(input("Ingrese mes de nacimiento (en numeros): "))


if (((dia >= 20) and (mes == 1)) or ((dia <= 19) and (mes == 2))):
    print("Tu signo zodiacal es: ACUARIO")

elif (((dia >= 19) and (mes == 2)) or ((dia <= 21 ) and (mes == 3))):
    print("Tu signo zodiacal es: PISCIS")

elif (((dia >= 21) and (mes == 3)) or ((dia <= 20) and (mes == 4))):
    print("Tu signo zodiacal es: ARIES")

elif (((dia >= 20) and (mes == 4)) or ((dia <= 21) and (mes == 5))):
    print("Tu signo zodiacal es: TAURO")

elif (((dia >= 21) and (mes == 5)) or ((dia <= 21) and (mes == 6))):
    print("Tu signo zodiacal es: GEMINI")

elif (((dia >= 21) and (mes == 6)) or ((dia <= 23) and (mes == 7))):
    print("Tu signo zodiacal es: CANCER")

elif (((dia >= 23) and (mes == 7)) or ((dia <= 23) and (mes == 8))):
    print("Tu signo zodiacal es: LEO")

elif (((dia >= 23) and (mes == 8)) or ((dia <= 23) and (mes == 9))):
    print("Tu signo zodiacal es: VIRGO")

elif (((dia >= 23) and (mes == 9)) or ((dia <= 23) and (mes == 10))):
    print("Tu signo zodiacal es: LIBRA")

elif (((dia >= 23) and (mes == 10)) or ((dia <= 22) and (mes == 11))):
    print("Tu signo zodiacal es: ESCORPIO")

elif (((dia >= 23) and (mes == 11)) or ((dia <= 22) and (mes == 12))):
    print("Tu signo zodiacal es: SAGITARIO")

elif (((dia >= 22) and (mes == 12)) or ((dia < 20) and (mes == 1))):
    print("Tu signo zodiacal es: CAPRICORNIO")
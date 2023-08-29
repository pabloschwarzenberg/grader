#Zodiaco
día = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese el número de mes de su nacimiento:"))

if ((mes == 12) and (día >= 21) or (mes == 1) and (día <= 19)):
    print("Tu signo es capricornio")

if ((mes == 1) and (día >= 20) or (mes == 2) and (día <= 18)):
    print("Tu signo es acuario")

if ((mes == 2) and (día >= 19) or (mes == 3) and (día <= 20)):
    print("Tu signo es piscis")

if ((mes == 3) and (día >= 21) or (mes == 4) and (día <= 20)):
    print("Tu signo es aries")

if ((mes == 4) and (día >= 21) or (mes == 5) and (día <= 20 )):
    print("Tu signo es tauro")

if ((mes == 5) and (día >= 21) or (mes == 6) and (día <= 20 )):
    print("Tu signo es geminis")

if ((mes == 6) and (día >= 21) or (mes == 7) and (día <= 20 )):
    print("Tu signo es cancer")

if ((mes == 7) and (día >= 21) or (mes == 8) and (día <= 21 )):
    print("Tu signo es leo")

if ((mes == 8) and (día >= 22) or (mes == 9) and (día <= 22 )):
    print("Tu signo es virgo")

if ((mes == 9) and (día >= 23) or (mes == 10) and (día <= 22 )):
    print("Tu signo es Libra")

if ((mes == 10) and (día >= 23) or (mes == 11) and (día <= 22 )):
    print("Tu signo es escorpio")

if ((mes == 11) and (día >= 23) or (mes == 12) and (día <= 20 )):
    print("Tu signo es sagitario")  
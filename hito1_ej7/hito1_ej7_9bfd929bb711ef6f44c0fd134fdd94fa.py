#Zodiaco
dia = int(input("Ingrese su dia de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento:"))

if ((mes == 12) and (dia >= 21) or (mes == 1) and (dia <= 19)):
    print("tu sigo es capricornio")

if ((mes == 1) and (dia >= 20) or (mes == 2) and (dia <= 18)):
    print("Tu signo es acuario")

if ((mes == 2) and (dia >= 19) or (mes == 3) and (dia <= 20)):
    print(" Tu signo es piscis")

if ((mes == 3) and (dia >= 21) or (mes == 4) and (dia <= 20)):
    print(" Tu signo es aries")

if ((mes == 4) and (dia >= 21) or (mes == 5) and (dia <= 20 )):
    print(" Tu signo es tauro")

if ((mes == 5) and (dia >= 21) or (mes == 6) and (dia <= 20 )):
    print(" Tu signo es geminis")

if ((mes == 6) and (dia >= 21) or (mes == 7) and (dia <= 20 )):
    print(" Tu signo es cancer")

if ((mes == 7) and (dia >= 21) or (mes == 8) and (dia <= 21 )):
    print(" Tu signo es leo")

if ((mes == 8) and (dia >= 22) or (mes == 9) and (dia <= 22 )):
    print(" Tu signo es virgo")

if ((mes == 9) and (dia >= 23) or (mes == 10) and (dia <= 22 )):
    print(" Tu signo es Libra")

if ((mes == 10) and (dia >= 23) or (mes == 11) and (dia <= 22 )):
    print(" Tu signo es escorpio")

if ((mes == 11) and (dia >= 23) or (mes == 12) and (dia <= 20 )):
    print("Tu signo es sagitario")

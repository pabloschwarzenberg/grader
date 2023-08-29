#Zodiaco
dia = eval(input("Ingrese día de su cumpleaños (1 al 31): "))
mes = eval(input("Ingrese mes de su cumpleaños (1 al 12): "))


if 21 < dia <= 31 and mes == 3:
    signo = "Aries"
elif 1 <= dia <= 20 and mes == 4:
    signo = "Aries"
elif 20 < dia <= 31 and mes == 4:
    signo = "Tauro"
elif 1 <= dia <= 21 and mes == 5:
    signo = "Tauro"
elif 21 < dia <= 31 and mes == 5:
    signo = "Geminis"
elif 1 <= dia <= 21 and mes == 6:
    signo = "Geminis"
elif 21 < dia <= 31 and mes == 6:
    signo = "Cancer"
elif 1 <= dia <= 23 and mes == 7:
    signo = "Cancer"
elif 23 < dia <= 31 and mes == 7:
    signo = "Leo"
elif 1 <= dia <= 23 and mes == 8:
    signo = "Leo"
elif 23 < dia <= 31 and mes == 8:
    signo = "Virgo"
elif 1 <= dia <= 23 and mes == 9:
    signo = "Virgo"
elif 23 < dia <= 31 and mes == 9:
    signo = "Libra"
elif 1 <= dia <= 23 and mes == 10:
    signo = "Libra"
elif 23 < dia <= 31 and mes == 10:
    signo = "Escopio"
elif 1 <= dia <= 22 and mes == 11:
    signo = "Escorpio"
elif 23 <= dia <= 31 and mes == 11:
    signo = "Sagitario"
elif 1 <= dia <= 22 and mes == 12:
    signo = "Sagitario"
elif 22 < dia <= 31 and mes == 12:
    signo = "Capricornio"
elif 1 <= dia <= 20 and mes == 1:
    signo = "Capricornio"
elif 20 < dia <= 31 and mes == 1:
    signo = "Acuario"
elif 1 <= dia <= 19 and mes == 2:
    signo = "Acuario"
elif 19 < dia <= 31 and mes == 2:
    signo = "Piscis"
elif 1 <= dia <= 21 and mes == 3:
    signo = "Piscis"

print("Signo Zodiacal es: ",signo)            
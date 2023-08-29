#Zodiaco
def signo_zodiaco(dia, mes):

    # Aries = 21/03 - 20/04
    if (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
        print("Aries")

    # Taurus = 21/04 - 21/05
    elif (dia >= 21 and mes == 4) or (dia <= 21 and mes == 5):
        print("Taurus")

    # Gemini = 21/05 - 21/06
    elif (dia >= 21 and mes == 5) or (dia <= 21 and mes == 6):
        print("Gemini")

    # Cancer = 21/06 - 23/07
    elif (dia >= 21 and mes == 6) or (dia <= 23 and mes == 7):
        print("Cancer")

    # Leo = 23/07 - 23/08
    elif (dia >= 23 and mes == 7) or (dia <= 23 and mes == 8):
        print("Leo")

    # Virgo = 23/08 - 23/09
    elif (dia >= 23 and mes == 8) or (dia <= 23 and mes == 9):
        print("Virgo")

    # Libra = 23/09 - 23/10
    elif (dia >= 23 and mes == 9) or (dia <= 23 and mes == 10):
        print("Libra")

    # Scorpio = 23/10 - 22/11
    elif (dia >= 23 and mes == 10) or (dia <= 22 and mes == 11):
        print("Scorpio")

    # Sagittarius = 22/11 - 22/12
    elif (dia >= 22 and mes == 11) or (dia <= 22 and mes == 12):
        print("Sagittarius")

    # Capricorn = 22/12 - 20/01
    elif (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
        print("Capricorn")

    # Acuario = 20/01 - 19/02
    elif (dia >= 20 and mes == 1) or (dia <= 19 and mes == 2):
        print("Acuario")

    # Piscis = 19/02 - 20/03
    elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
        print("Piscis")

print( "Ingresa los datos de tu cumpleaños (Numeros): ")
dia = int(input("Dia: "))
mes = int(input("Mes: "))
signo_zodiaco(dia, mes)
print("\n")
print("Espero que te haya gustado este programa")     
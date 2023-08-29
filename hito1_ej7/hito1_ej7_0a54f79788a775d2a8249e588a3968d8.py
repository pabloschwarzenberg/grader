#Zodiaco
dia=int(input("ingrese dia del cumpleaños: "))
mes=int(input("ingrese mes del cumpleaños: "))

if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 19 ):
    print("tu signo es Acuario") 
if (mes == 2 and dia >= 19) or (mes == 3 and dia <= 21 ):
    print("tu signo es Picis")
if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20 ):
    print("tu signo es Aries")
if (mes == 4 and dia >= 20) or (mes == 5 and dia <= 21 ):
    print("tu signo es Taurus")
if (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21 ):
    print("tu signo es Gemini")
if (mes == 6 and dia >= 21) or (mes == 7 and dia <= 23 ):
    print("tu signo es Cancer")
if (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23 ):
    print("tu signo es Leo")
if (mes == 8 and dia >= 23) or (mes == 9 and dia <= 23 ):
    print("tu signo es Virgo")
if (mes == 9 and dia >= 23) or (mes == 10 and dia <= 23 ):
    print("tu signo es Libra")
if (mes == 10 and dia >= 23) or (mes == 11 and dia <= 22 ):
    print("tu signo es Scorpio")
if (mes == 11 and dia >= 23) or (mes == 12 and dia <= 22 ):
    print("tu signo es Sagittarius")
if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20 ):
    print("tu signo es Capricorn")
if (mes >= 13) or ( dia > 31):
    print("mes o dia ingresado incorrectamente vuelve a intentar")

n = int(input("Ingrese su día y mes de nacimiento sin espacios:  "))
signo = ""

while n > 0 and n < 3113:
    if n <=2004 and n >= 2103:
        signo = "Aries"
        break
    elif n <=2105 and n >= 2104:
        signo = "Tauro"
        break
    elif n <=2106 and n >= 2205:
        signo = "Geminis"
        break
    elif n <=2307 and n >= 2206:
        signo = "Cancer"
        break
    elif n <=2308 and n >= 2407:
        signo = "Leo"
        break
    elif n <=2309 and n >= 2408:
        signo = "Virgo"
        break
    elif n <=2310 and n >= 2409:
        signo = "Libra"
        break
    elif n <=2211 and n >= 2410:
        signo = "Escorpio"
        break
    elif n <=2212 and n >= 2311:
        signo = "Sagitario"
        break
    elif n <= 2001 and n >= 2312:
        signo = "Capricornio"
        break
    elif n <=1902 and n >= 2101:
        signo = "Acuario"
        break
    elif n <=2104 and n >= 2002:
        signo = "Piscis"
        break
    else:
        print("La fecha ingresada no es la correcta por favor intentelo de nuevo:  ")

print("Su signo zodiacal es:  " , signo)

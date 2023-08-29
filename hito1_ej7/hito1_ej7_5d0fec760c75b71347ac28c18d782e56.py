#Zodiaco
 print("A continuacion determinaremos su signo zodiacal de acuerdo a su mes y dia de nacimiento")
dia = int(input("Introduzca su dia de nacimiento: "))
mes = int(input("Introduzca su mes de nacimiento : "))

enero = 1
febrero = 2
marzo = 3
abril = 4
mayo = 5
junio = 6
julio = 7
agosto = 8
septiembre = 9
octubre = 10
noviembre = 11
diciembre = 12

if 21<=dia<=30 and mes == marzo:
    print("Aries")

elif 1<=dia<=19 and mes == abril:
    print("Aries")

elif 20<=dia<=30 and mes == abril:
    print("Taurus")

elif 1<=dia<=20 and mes == mayo:
    print("Taurus")

elif 21<=dia<=30 and mes == mayo:
    print("Gemini")

elif 1<=dia<=21 and mes == junio:
    print("Gemini")

elif 22<=dia<=30 and mes == junio:
    print("Cancer")

elif 1<=dia<=22 and mes == julio:
    print("Cancer")

elif 23<=dia<=30 and mes ==julio:
    print("Leo")

elif 1<=dia<=23 and mes == agosto:
    print("Leo")

elif 24<=dia<=30 and mes == agosto:
    print("Virgo")

elif 1<=dia<22 and mes == septiembre:
    print("Virgo")

elif 23<=dia<=30 and mes == septiembre:
    print("Libra")

elif 1<=dia<=23 and mes == octubre:
    print("Libra")

elif 24<=dia<=30 and mes == octubre:
    print("Scorpio")

elif 1<=dia<=22 and mes == noviembre:
    print("Scorpio")

elif 23<=dia<=30 and mes == noviembre:
    print("Sagitarius")

elif 1<=dia<=22 and mes == diciembre:
    print("Sagitarius")

elif 23<=dia<=30 and mes == diciembre:
    print("Capricorn")

elif 1<=dia<=20 and mes == enero:
    print("Capricorn")

elif 21<=dia<=30 and mes == enero:
    ("Aquarius")

elif 1<=dia<=18 and mes == febrero:
    print("Aquarius")

elif 19<=dia<=30 and mes == febrero:
    print("Pisces")

elif 1<=dia<=20 and mes == marzo:
    print("Pisces")     
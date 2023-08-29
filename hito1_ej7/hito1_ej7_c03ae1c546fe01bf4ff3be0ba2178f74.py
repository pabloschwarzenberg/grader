#Zodiaco
Dia=int(input(""))
Mes=int(input(""))
if Mes == 2:
    Dia= Dia + 31
if Mes == 3:
    Dia= Dia + 59
if Mes == 4:
    Dia= Dia + 90
if Mes == 5:
    Dia= Dia + 120
if Mes == 6:
    Dia= Dia + 151
if Mes == 7:
    Dia= Dia + 181
if Mes == 8:
    Dia= Dia + 212
if Mes == 9:
    Dia= Dia + 243
if Mes == 10:
    Dia= Dia + 273
if Mes == 11:
    Dia= Dia + 304
if Mes == 12:
    Dia= Dia + 334
if 79<Dia<111:
    print("Aries")
if 110<Dia<142:
    print("Tauro")
if 141<Dia<173:
    print("Geminis")
if 172<Dia<204:
    print("Cancer")
if 203<Dia<235:
    print("Leo")
if 234<Dia<267:
    print("Virgo")
if 266<Dia<297:
    print("Libra")
if 296<Dia<327:
    print("Escorpion")
if 326<Dia<356:
    print("Sagitario")
if Dia>335 or Dia<21:
    print("Capricornio")
if 20<Dia<48:
    print("Acuario")
else:
    print("Piscis")

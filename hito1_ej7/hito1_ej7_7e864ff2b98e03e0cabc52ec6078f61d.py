#Zodiaco
dia=int(input("Dia: "))
mes=int(input("Mes: "))

w=(100*mes+dia)
z = int(w)

if 321<=z<=420:
    print("Aries")
elif 421<=z<=521:
    print("Tauro")
elif 522<=z<=621:
    print("Geminis")
elif 622<=z<=722:
    print("Cancer")
elif 723<=z<=822:
    print("Leo")
elif 823<=z<=923:
    print("Virgo")
elif 924<=z<=1023:
    print("Libra")
elif 1024<=z<=1122:
    print("Scorpio")
elif 1123<=z<=1221:
    print("Sagitario")
elif 121<=z<=219:
    print("Acuario")
elif 220<=z<=320:
    print("Piscis")
else:
    print("Capricornio")
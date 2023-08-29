#Zodiaco
dia=int(input("Ingrese dia de cumpleaños: "))
mes=int(input("Ingrese numero de mes de cumpleaños: "))
variable=100*mes+dia
if 321<=variable<=420:
    print("Aries")
elif 421<=variable<=521:
    print("Tauro")
elif 522<=variable<=621:
    print("Geminis")
elif 622<=variable<=722:
    print("Cancer")
elif 723<=variable<=822:
    print("Leo")
elif 823<=variable<=923:
    print("Virgo")
elif 924<=variable<=1023:
    print("Libra")
elif 1024<=variable<=1122:
    print("Escorpio")
elif 1123<=variable<=1221:
    print("Sagitario")
elif 121<=variable<=219:
    print("Acuario")
elif 220<=variable<=320:
    print("Piscis")
else:
    print("Capricornio")    
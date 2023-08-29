#Zodiaco
from os import system
system("cls")

dia = int(input("Chantame el dia: "))
mes = int(input("Y el mes po, y te dire quien eres: "))

if dia>=21 and mes == 3 or dia<=20 and mes ==4:
    print("ARIES")
elif dia>=21 and mes == 4 or dia<=20 and mes ==5:
    print("TAURO")
elif dia>=21 and mes ==5 or dia<=20 and mes == 6:
    print("GEMINIS")
elif dia>= 21 and mes ==6 or dia<=22 and mes ==7:
    print("CANCER")
elif dia>=23 and mes == 7 or dia<=23 and mes ==8:
    print("LEO")
elif dia>=24 and mes ==8 or dia<=23 and mes ==9:
    print("VIRGO")
elif dia>=23 and mes ==9 or dia<=22 and mes==10:
    print("LIBRA")
elif dia>=23 and mes==10 or dia<=22 and mes==11:
    print("ESCORPIO")
elif dia>=23 and mes==11 or dia<=21 and mes==12:
    print("SAGITARIO")
elif dia>=22 and mes==12 or dia<=20 and mes==1:
    print("CAPRICORNIO")
elif dia>=21 and mes==1 or dia<=19 and mes==2:
    print("ACUARIO")
else:
    print("PSISCIS")  
#Zodiaco
#Entradas
dia_cumpleanos  = int(input("Ingrese el día de su cumpleanos: (1-31) "))
mes_cumpleanos  = int(input("Ingrese el mes de su cumpleanos: (1-12) "))

if (dia_cumpleanos>=21 and mes_cumpleanos == 3) or (dia_cumpleanos<=20 and mes_cumpleanos==4):
    print("Tu signo Zodiacal es: Aries")

elif (dia_cumpleanos>=20 and mes_cumpleanos == 4) or (dia_cumpleanos<=21 and mes_cumpleanos==5):
    print("Tu signo Zodiacal es: Tauro")

elif (dia_cumpleanos>=21 and mes_cumpleanos == 5) or (dia_cumpleanos<=21 and mes_cumpleanos==6):
    print("Tu signo Zodiacal es: Geminis")

elif (dia_cumpleanos>=21 and mes_cumpleanos == 6) or (dia_cumpleanos<=23 and mes_cumpleanos==7):
    print("Tu signo Zodiacal es: Cáncer")

elif (dia_cumpleanos>=23 and mes_cumpleanos == 7) or (dia_cumpleanos<=23 and mes_cumpleanos==8):
    print("Tu signo Zodiacal es: Leo")

elif (dia_cumpleanos>=23 and mes_cumpleanos == 8) or (dia_cumpleanos<=23 and mes_cumpleanos==9):
    print("Tu signo Zodiacal es: Virgo")
     
elif (dia_cumpleanos>=23 and mes_cumpleanos == 9) or (dia_cumpleanos<=23 and mes_cumpleanos==10):
    print("Tu signo Zodiacal es: Libra")   

elif (dia_cumpleanos>=23 and mes_cumpleanos == 10) or (dia_cumpleanos<=22 and mes_cumpleanos==11):
    print("Tu signo Zodiacal es: Escorpio")  

elif (dia_cumpleanos>=23 and mes_cumpleanos == 11) or (dia_cumpleanos<=22 and mes_cumpleanos==12):
    print("Tu signo Zodiacal es: Sagitario")

elif (dia_cumpleanos>=22 and mes_cumpleanos == 12) or (dia_cumpleanos<=20 and mes_cumpleanos==1):
    print("Tu signo Zodiacal es: Carpicornio")

elif (dia_cumpleanos>=20 and mes_cumpleanos == 1) or (dia_cumpleanos<=19 and mes_cumpleanos==2):
    print("Tu signo Zodiacal es: Acuario")

elif (dia_cumpleanos>=19 and mes_cumpleanos == 2) or (dia_cumpleanos<=21 and mes_cumpleanos==3):
    print("Tu signo Zodiacal es: Piscis")
else:
    print("Fecha incorrecta")
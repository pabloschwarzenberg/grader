#Zodiaco
day=int(input("Indique el día de su nacimiento: "))
mon=int(input("Indique el mes de su nacimiento (Enero = 1): "))

if day==0 or mon==0 or day>31 or mon>12:
    print("Datos inválidos.")
elif (day>=21 and mon==3) or (day<=20 and mon==4):
    print("Aries(♈)")
elif (day>=21 and mon==4) or (day<=21 and mon==5):
    print("Tauro(♉)")
elif (day>=22 and mon==5) or (day<=23 and mon==6):
    print("Géminis(♊)")
elif (day>=24 and mon==6) or (day<=23 and mon==7):
    print("Cáncer(♋)")
elif (day>=24 and mon==7) or (day<=23 and mon==8):
    print("Leo(♌)")
elif (day>=24 and mon==8) or (day<=22 and mon==9):
    print("Virgo(♍)")
elif (day>=23 and mon==9) or (day<=23 and mon==10):
    print("Libra(♎)")
elif (day>=24 and mon==10) or (day<=22 and mon==11):
    print("Escorpio(♏)")
elif (day>=23 and mon==11) or (day<=21 and mon==12):
    print("Sagitario(♐)")
elif (day>=22 and mon==12) or (day<=19 and mon==1):
    print("Capricornio(♑)")
elif (day>=20 and mon==1) or (day<=18 and mon==2):
    print("Acuario(♒)")
elif (day>=19 and mon==2) or (day<=20 and mon==3):
    print("Piscis(♓)")  
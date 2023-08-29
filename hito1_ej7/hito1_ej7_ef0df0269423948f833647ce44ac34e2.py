#Zodiaco
dias= int(input("Ingrese dia de nacimiento: "))
mes= int(input("Ingrese mes de nacimiento: "))

def calendario_zodiaco (dias,mes):
    if mes <1 and mes >12:
        return print ("mes mal ingresado")
    if dias <1 and dias >31:
        return print ("dia mal ingresado")
    if (dias >=21 and dias <=31 and mes==3) or (dias >=1 and dias <20 and mes==4):
        return print ("Aries")
    if (dias >=20 and dias <=30 and mes==4) or (dias >=1 and dias <21 and mes==5):
        return print ("Tauro")
    if (dias >=21 and dias <=31 and mes==5) or (dias >=1 and dias <21 and mes==6):
        return print ("Gemenis")
    if (dias >=21 and dias <=30 and mes==6) or (dias >=1 and dias <23 and mes==7):
        return print ("Cancer")
    if (dias >=23 and dias <=31 and mes==7) or (dias >=1 and dias <23 and mes==8):
        return print ("Leo")
    if (dias >=23 and dias <=31 and mes==8) or (dias >=1 and dias <23 and mes==9):
        return print ("Virgo")
    if (dias >=23 and dias <=30 and mes==9) or (dias >=1 and dias <23 and mes==10):
        return print ("Libra")
    if (dias >=23 and dias <=31 and mes==10) or (dias >=1 and dias <22 and mes==11):
        return print ("Escorpion")
    if (dias >=23 and dias <=30 and mes==11) or (dias >=1 and dias <22 and mes==12):
        return print ("Sagitario")
    if (dias >=22 and dias <=31 and mes==12) or (dias >=1 and dias <20 and mes==1):
        return print ("Capricornio")
    if (dias >=20 and dias <=31 and mes==1) or (dias >=1 and dias <19 and mes==2):
        return print ("Acuario")
    if (dias >=19 and dias <=28 and mes==2) or (dias >=1 and dias <21 and mes==3):
        return print ("Piscis")

calendario_zodiaco (dias,mes)      
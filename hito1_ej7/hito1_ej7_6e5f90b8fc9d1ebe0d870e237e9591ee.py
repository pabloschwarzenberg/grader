#Zodiaco
dia=int(input("Dia de su Cumpleaños"))
mes=int(input("Mes de su cumpleaños(numero)"))

if(dia<=20 and mes==1):
    print("Capricornio")
elif(dia>20 and mes==1):
    print("Acuario")
elif(dia<=19 and mes==2):
    print("Acuario")
elif(dia>19and mes==2):
    print("Piscis")
elif(dia<=20 and mes==3):
    print("Piscis")
elif(dia>20 and mes==3):
    print("Aries")
elif(dia<=20 and mes==4):
    print("Aries")
elif(dia>20 and mes==4):
    print("Tauro")
elif(dia<=21 and mes==5):
    print("Tauro")
elif(dia>21 and mes==5):
    print("Geminis")
elif(dia<=22 and mes==6):
    print("Geminis")
elif(dia>22 and mes==6):
    print("Cancer")
elif(dia<=22 and mes==7):
    print("Cancer")
elif(dia>22 and mes==7):
    print("Leo")
elif(dia<=23 and mes ==8):
    print("Leo")
elif(dia>23 and mes==8):
    print("Virgo")
elif(dia<=23 and mes==9):
    print("Virgo")
elif(dia>23 and mes==9):
    print("Libra")
elif(dia<=23 and mes==10):
    print("Libra")
elif(dia>23 and mes==10):
    print("Escorpio")
elif(dia<=22 and mes==11):
    print("Escorpio")
elif(dia>22 and mes==11):
    print("Sagitario")
elif(dia<=21 and mes==12):
    print("Sagitario")
else:
    if(dia>21 and mes==12):
        print("Capricornio")     
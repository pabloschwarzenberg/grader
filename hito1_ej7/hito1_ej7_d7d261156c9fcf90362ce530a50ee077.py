#Signo del Zodiaco
dia=int(input("Ingrese el día de su cumpleaños:"))
mes=int(input("Ingrese el mes de su cumpleaños:"))
if (mes==3 and 21<=dia<=31) or (mes==4 and 1<=dia<=20):
    print("Aries")
elif (mes==3 and 21<=dia<=31) or (mes==5 and 1<=dia<=21):
    print("Tauro")
elif (mes==5 and 22<=dia<=31) or (mes==6 and 1<=dia<=21):
    print("Gemini")
elif (mes==6 and 22<=dia<=30) or (mes==7 and 1<=dia<=22):
    print("Cáncer")
elif (mes==7 and 23<=dia<=31) or (mes==8 and 1<=dia<=22):
    print("Leo")
elif (mes==8 and 23<=dia<=31) or (mes==9 and 1<=dia<=23):
    print("Virgo")
elif (mes==9 and 24<=dia<=30) or (mes==10 and 1<=dia<=23):
    print("Libra")
elif (mes==10 and 24<=dia<=31) or (mes==11 and 1<=dia<=22):
    print("Escorpio")
elif (mes==11 and 23<=dia<=30) or (mes==12 and 1<=dia<=21):
    print("Sagitario")
elif (mes==12 and 22<=dia<=31) or (mes==1 and 1<=dia<=20):
    print("Capricornio")
elif (mes==1 and 21<=dia<=31) or (mes==2 and 1<=dia<=19):
    print("Acuario")
elif (mes==2 and 20<=dia<=28) or (mes==3 and 1<=dia<=20):
    print("Piscis")
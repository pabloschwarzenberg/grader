#Zodiaco
dia=int(input("Ingresa tu mes de nacimiento (En numeros): "))
mes=int(input("Ingresa tu día de nacimiento (En numeros): "))

if mes==1:
    if dia<=20:
        print("capricornio")
    else:
        print("acuario")
elif mes==2:
    if dia<=19:
        print("acuario")
    else:
        print("piscis")
elif mes==3:
    if dia<=20:
        print("piscis")
    else:
        print("aries")
elif mes==4:
    if dia<=20:
        print("aries")
    else:
        print("tauro")
elif mes==5:
    if dia<=21:
        print("tauro")
    else:
        print("geminis")
elif mes==6:
    if dia<=21:
        print("geminis")
    else:
        print("cancer")
elif mes==7:
    if dia<=22:
        print("cancer")
    else:
        print("leo")
elif mes==8:
    if dia<=22:
        print("leo")
    else:
        print("virgo")
elif mes==9:
    if dia<=23:
        print("virgo")
    else:
        print("libra")
elif mes==10:
    if dia<=23:
        print("libra")
    else:
        print("escorpion")
elif mes==11:
    if dia<=22:
        print("escorpion")
    else:
        print("sagitario")
elif mes==12:
    if dia<=21:
        print("sagitario")
    else:
        print("sapricornio")
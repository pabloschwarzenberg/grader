#Zodiaco
print("Para conocer tu signo del zodiaco...")
dia = int(input("Ingresa el día de tu cumpleaños:"))
mes = int(input("Ingresa el mes de tu cumpleaños:"))
if (int(mes)==1 and 20<=dia<=31) or (int(mes)==2 and 1<=dia<=19):
    print("Su signo del zodiaco es: Acuario")
elif (int(mes)==2 and 20<=dia<=30) or (int(mes)==3 and 1<=dia<=20):
    print("Su signo del zodiaco es: Picis")
elif (int(mes)==3 and 21<=dia<=31) or (int(mes)==4 and 1<=dia<=19):
    print("Su signo del zodiaco es: Aries")
elif (int(mes)==4 and 20<=dia<=30) or (int(mes)==5 and 1<=dia<=20):
    print("Su signo del zodiaco es: Tauro")
elif (int(mes)==5 and 21<=dia<=31) or (int(mes)==6 and 1<=dia<=20):
    print("Su signo del zodiaco es: Geminis")
elif (int(mes)==6 and 21<=dia<=30) or (int(mes)==7 and 1<=dia<=22):
    print("Su signo del zodiaco es: Cancer")
elif (int(mes)==7 and 23<=dia<=31) or (int(mes)==8 and 1<=dia<=22):
    print("Su signo del zodiaco es: Leo")
elif (int(mes)==8 and 23<=dia<=31) or (int(mes)==9 and 1<=dia<=22):
    print("Su signo del zodiaco es: Virgo")
elif (int(mes)==9 and 23<=dia<=30) or (int(mes)==10 and 1<=dia<=22):
    print("Su signo del zodiaco es: Libra")
elif (int(mes)==10 and 23<=dia<=31) or (int(mes)==11 and 1<=dia<=21):
    print("Su signo del zodiaco es: Escorpio")
elif (int(mes)==11 and 22<=dia<=30) or (int(mes)==12 and 1<=dia<=21):
    print("Su signo del zodiaco es: Sagitario")
elif (int(mes)==12 and 22<=dia<=31) or (int(mes)==1 and 1<=dia<=19):
    print("Su signo del zodiaco es: Capricornio")
else:
    print("Opción no válida")
#Zodiaco
dia=int(input("Ingrese el día de su cumpleaños:"))
mes=int(input("Ingrese el mes de su cumpleaños:"))
if  (mes==3 and dia>=21)or (mes==4 and dia<20):
    print("Aries")
if (mes==4 and dia>=20) or (mes==5 and dia<21):
    print("Taurus")
if (mes==5 and dia>=21) or (mes==6 and dia<21):
    print("Gemini")
if (mes==6 and dia>=21) or (mes==7 and dia<23):
    print("Cancer")
if (mes==7 and dia>=23) or (mes==8 and dia<23):
    print("Leo")
if (mes==8 and dia>=23) or (mes==9 and dia<23):
    print("Virgo")
if (mes==9 and dia>=23) or (mes==10 and dia<23):
    print("Libra")
if (mes==10 and dia>=23) or (mes==11 and dia<=22):
    print("Escorpio")
if (mes==11 and dia>=23) or (mes==12 and dia<22):
    print("Saggitarius")
if (mes==12 and dia>=22) or (mes==1 and dia<20):
    print("Capricorn")
if (mes==1 and dia>=20)or (mes==2 and dia<19):
    print("Aquarius")
if (mes==2 and dia>=19) or (mes==3 and dia<21):
    print("Piscis")
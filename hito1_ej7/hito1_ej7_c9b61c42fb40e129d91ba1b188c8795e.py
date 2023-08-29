#Zodiaco
dia = int(input("Ingrese dia de cumpleaños: "))
while not(dia>0 and dia<=31):
    dia = int(input("Ingrese una fecha válida: "))
mes = int(input("Ingrese número del mes: "))
while not(mes>=1 and mes<=12):
    mes = int(input("Ingrese un mes válido: "))
if (dia>=21 and mes == 3) or (dia<20 and mes == 4):
    a = "Aries"
    print("Su signo zodiacal es:",a)
elif (dia>=20 and mes == 4) or (dia<21 and mes == 5):
    t = "Tauro"
    print("Su signo zodiacal es:",t)
elif (dia>=21 and mes == 5) or (dia<21 and mes == 6):
    g = "Geminis"
    print("Su signo zodiacal es:",g)
elif (dia>=21 and mes == 6) or (dia<23 and mes == 7):
    c = "Cancer"
    print("Su signo zodiacal es:",c)
elif (dia>=23 and mes == 7) or (dia<23 and mes == 8):
    l = "Leo"
    print("Su signo zodiacal es:",l)
elif (dia>=23 and mes == 8) or (dia<23 and mes == 9):
    v = "Virgo"
    print("Su signo zodiacal es:",v)
elif (dia>=23 and mes == 9) or (dia<23 and mes == 10):
    l = "Libra"
    print("Su signo zodiacal es:",l)
elif (dia>=23 and mes == 10) or (dia<22 and mes == 11):
    e = "Escorpión"
    print("Su signo zodiacal es:",e)
elif (dia>=22 and mes == 11) or (dia<22 and mes == 12):       
    s = "Sagitario"
    print("Su signo zodiacal es:",s)
elif (dia>=22 and mes == 12) or (dia<20 and mes == 1):
    c ="Capricornio"
    print("Su signo zodiacal es:",c)
elif (dia>=20 and mes == 1) or (dia<19 and mes == 2):
    a ="Acuario"
    print("Su signo zodiacal es:",a)
else:
    p ="Piscis"
    print("Su signo zodiacal es:",p)      
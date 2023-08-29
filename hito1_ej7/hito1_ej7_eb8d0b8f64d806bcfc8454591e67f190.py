#Zodiaco
dia = int(input("ingresa tu dia de nacimiento:"))
mes = int(input("ingresa tu mes de nacimiento con números:"))
if 21<=dia<=31 and mes==3 or 1<=dia<=20 and mes==4:
    print ("Tu signo zodiacal es Aries")
elif 21<=dia<=30 and mes==4 or 1<=dia<=21 and mes==5:
    print ("Tu signo zodiacal es Tauro")
elif 22<=dia<=31 and mes==5 or 1<=dia<=21 and mes==6:
    print ("Tu signo zodiacal es Geminis")
elif 22<=dia<=30 and mes==6 or 1<=dia<=22 and mes==7:
    print ("Tu signo zodiacal es Cancer")
elif 23<=dia<=31 and mes==7 or 1<=dia<=22 and mes==8:
    print ("Tu signo zodiacal es Leo")
elif 23<=dia<=31 and mes==8 or 1<=dia<=23 and mes==9:
    print ("Tu signo zodiacal es Virgo")
elif 24<=dia<=30 and mes==9 or 1<=dia<=23 and mes==10:
    print ("Tu signo zodiacal es Libra")
elif 24<=dia<=31 and mes==10 or 1<=dia<=22 and mes==11:
    print ("Tu signo zodiacal es Scorpio")
elif 23<=dia<=30 and mes==11 or 1<=dia<=21 and mes==12:
    print ("Tu signo zodiacal es Sagitario")
elif 22<=dia<=31 and mes==12 or 1<=dia<=20 and mes==1:
    print ("Tu signo zodiacal es Capricornio")
elif 21<=dia<=31 and mes==1 or 1<=dia<=19 and mes==2:
    print ("Tu signo zodiacal es Acuario")
elif 20<=dia<=28 and mes==2 or 1<=dia<=20 and mes==3:
    print ("Tu signo zodiacal es Piscis")
elif dia==29 and mes==2:
    print ("Felicidades, naciste en año bisiesto, eres Piscis")
    
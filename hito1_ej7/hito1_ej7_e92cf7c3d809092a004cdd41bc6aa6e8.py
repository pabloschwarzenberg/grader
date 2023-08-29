#Zodiaco
dia = int(input("Favor ingrese dia de cumpleaños: "))
mes = int(input("Favor ingrese mes de cumpleaños: "))

if dia > 21 or dia < 20 and mes == 3 or mes == 4:
    signo = "Aries"
    print ("Tu signo zodiacal es,",signo)
elif dia > 20 or dia < 21 and mes == 4 or mes == 5:
    signo = "Tauro"
    print ("Tu signo zodiacal es",signo)
elif dia > 21 or dia < 21 and mes == 5 or mes == 6:
    signo ="Gemini"
    print ("Tu signo zodiacal es",signo)
elif dia > 21 or dia < 23 and mes == 6 or mes == 7:
    signo ="Cancer"
    print ("Tu signo zodiacal es",signo)
elif dia > 23 or dia < 23 and mes == 7 or mes == 8:
    signo ="Leo"
    print ("Tu signo zodiacal es",signo)
elif dia > 23 or dia < 23 and mes == 8 or mes == 9:
    signo ="Virgo"
    print ("Tu signo zodiacal es",signo)
elif dia > 23 or dia < 23 and mes == 9 or mes == 10:
    signo ="Libra"
    print ("Tu signo zodiacal es",signo)
elif dia > 23 or dia < 22 and mes == 10 or mes == 11:
    signo ="Escorpio"
    print ("Tu signo zodiacal es",signo)
elif dia > 23 or dia < 22 and mes == 11 or mes == 12:
    signo ="Sagitario"
    print ("Tu signo zodiacal es",signo)
elif dia > 22 or dia < 20 and mes == 12 or mes == 1:
    signo ="Capricornio"
    print ("Tu signo zodiacal es",signo)
elif dia > 20 or dia < 19 and mes == 1 or mes == 2:
    signo ="Acuario"
    print ("Tu signo zodiacal es",signo)
elif dia > 19 or dia < 21 and mes == 2 or mes == 3:
    signo ="Piscis"
    print ("Tu signo zodiacal es",signo)
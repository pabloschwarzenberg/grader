#Zodiaco
print("Este es un programa que indica tu signo del zodiaco.\nDebes ingresar el dia y mes como un número entero. por ejemplo: día=9 ; septiembre=9")

dia = int(input("Dime el dia que naciste:",))
mes = int(input("Dime el mes que naciste:",))

if (dia>=21 and mes==3) or (dia<=20 and mes==4):
    print("Tu signo del zodiaco es 'ARIES'")
elif (dia>=21 and mes==4) or (dia<=21 and mes==5):
    print("Tu signo zodiacal es 'TAURO'")
elif (dia>=22 and mes==5) or (dia<=21 and mes==6):
    print("Tu signo del zodiaco es 'GEMINIS'")
elif (dia>=21 and mes==6) or (dia<=23 and mes==7):
    print("Tu signo zodiacal es 'CÁNCER'")
elif (dia>=24 and mes==7) or (dia<=23 and mes==8):
    print("Tu signo zodiacal es 'LEO'")
elif (dia>=24 and mes==8) or (dia<=23 and mes==9):
    print("Tu signo zodiacal es 'VIRGO'")
elif (dia>=24 and mes==9) or (dia<=23 and mes==10):
    print("Tu signo zodiacal es 'LIBRA'")
elif (dia>=24 and mes==10) or (dia<=22 and mes==11):
    print("Tu signo zodiacal es 'ESCORPIO'")
elif (dia>=23 and mes==11) or (dia<=21 and mes==12):
    print("Tu signo zodiacal es 'SAGITARIO'")
elif (dia>=22 and mes==12) or (dia<=20 and mes==1):
    print("Tu signo zodiacal es 'CAPRICORNIO'")
elif (dia>=21 and mes==1) or (dia<=19 and mes==2):
    print("Tu signo zodiacal es 'ACUARIO'")
elif (dia>=20 and mes==2) or (dia<=20 and mes==3):
    print("Tu signo zodiacal es 'PISCIS'")
else:
    print("ingresa una fecha valida.")
#Zodiaco
dia = int(input("Escribe el día (numero):"))
mes = int(input("Escribe el mes (numero):"))

if((mes==3) and (dia>=21)) or ((mes==4) and (dia<=20)):
    signo = 'aries'
    print("Tu signo es:",signo)
elif((mes==4) and (dia>=20)) or ((mes==5) and (dia<=21)):
    signo = 'taurus'
    print("Tu signo es:",signo)
elif((mes==5) and (dia>=21)) or ((mes==6) and (dia<=21)):
    signo = 'Gemini'
    print("Tu signo es:",signo)
elif((mes==6) and (dia>=21)) or ((mes==7) and (dia<=23)):
    signo = 'Cancer'
    print("Tu signo es:",signo)
elif((mes==7) and (dia>=23)) or ((mes==8) and (dia<=23)):
    signo = 'Leo'
    print("Tu signo es:",signo)
elif((mes==8) and (dia>=23)) or ((mes==9) and (dia<=23)):
    signo = 'Virgo'
    print("Tu signo es:",signo)
elif((mes==9) and (dia>=23)) or ((mes==10) and (dia<=23)):
    signo = 'Libra'
    print("Tu signo es:",signo)
elif((mes==10) and (dia>=23)) or ((mes==11) and (dia<=22)):
    signo = 'Scorpio'
    print("Tu signo es:",signo)
elif((mes==11) and (dia>=22)) or ((mes==12) and (dia<=22)):
    signo = 'Sagitario'
    print("Tu signo es:",signo)
elif((mes==12) and (dia>=22)) or ((mes==1) and (dia<=20)):
    signo = 'Capricornio'
    print("Tu signo es:",signo)
elif((mes==1) and (dia>=22)) or ((mes==2) and (dia<=19)):
    signo = 'Aquarius'
    print("Tu signo es:",signo)
elif((mes==2) and (dia>=19)) or ((mes==3) and (dia<=21)):
    signo = 'Piscis'
    print("Tu signo es:",signo)

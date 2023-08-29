dia=int(input("Ingrese dia de nacimiento: "))
mes=int(input("Ingrese mes de nacimiento: "))
if ((mes==3) and (dia>=21)) or ((mes==4) and (dia<=19)):
    print ("Su signo zodiacal es Aries")
elif ((mes==4) and (dia>=20)) or ((mes==5) and (dia<=20)):
    print ("Su signo zodiacal es Tauro")
elif ((mes==5) and (dia>=21)) or ((mes==6) and (dia<=21)):
    print ("Su signo zodiacal es Geminis")
elif ((mes==6) and (dia>=22)) or ((mes==7) and (dia<=22)):
    print ("Su signo zodiacal es Cancer")
elif ((mes==7) and (dia>=23)) or ((mes==8) and (dia<=23)):
    print ("Su signo zodiacal es Leo")
elif ((mes==8) and (dia>=24)) or ((mes==9) and (dia<=22)):
    print ("Su signo zodiacal es Virgo")
elif ((mes==9) and (dia>=23)) or ((mes==10) and (dia<=23)):
    print ("Su signo zodiacal es Libra")
elif ((mes==10) and (dia>=24)) or ((mes==11) and (dia<=22)):
    print ("Su signo zodiacal es Escorpio")
elif ((mes==11) and (dia>=23)) or ((mes==12) and (dia<=22)):
    print ("Su signo zodiacal es Sagitario")
elif ((mes==12) and (dia>=23)) or ((mes==1) and (dia<=20)):
    print ("Su signo zodiacal es Capricornio")
elif ((mes==1) and (dia>=21)) or ((mes==2) and (dia<=18)):
    print ("Su signo zodiacal es Acuario")
elif ((mes==2) and (dia>=19)) or ((mes==3) and (dia<=20)):
    print ("Su signo zodiacal es Piscis")    
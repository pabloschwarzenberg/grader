#Zodiaco
dia=int(input("Ingrese su día de cumpleaños: "))
mes=int(input("Ingrese su mes de cumpleaños: "))

if ((mes==3) and (dia>=21)) or ((mes==4) and (dia<=20)):
    signo = "Aries"
    print("Su signo es ", signo)
elif ((mes==4) and (dia>=21)) or ((mes==5) and (dia<=21)):
    signo = "Tauro"
    print("Su signo es ", signo)
elif ((mes==5) and (dia>=22)) or ((mes==6) and (dia<=21)):
    signo = "Géminis"
    print("Su signo es ", signo)
elif ((mes==6) and (dia>=22)) or ((mes==7) and (dia<=23)):
    signo = "Cáncer"
    print("Su signo es ", signo)
elif ((mes==7) and (dia>=24)) or ((mes==8) and (dia<=23)):
    signo = "Leo"
    print("Su signo es ", signo)
elif ((mes==8) and (dia>=24)) or ((mes==9) and (dia<=23)):
    signo = "Virgo"
    print("Su signo es ", signo)
elif ((mes==9) and (dia>=24)) or ((mes==10) and (dia<=23)):
    signo = "Libra"
    print("Su signo es ", signo)
elif ((mes==10) and (dia>=24)) or ((mes==11) and (dia<=22)):
    signo = "Escorpio"
    print("Su signo es ", signo)
elif ((mes==11) and (dia>=23)) or ((mes==12) and (dia<=21)):
    signo = "Sagitario"
    print("Su signo es ", signo)
elif ((mes==12) and (dia>=22)) or ((mes==1) and (dia<=20)):
    signo = "Capricornio"
    print("Su signo es ", signo)
elif ((mes==1) and (dia>=21)) or ((mes==2) and (dia<=19)):
    signo = "Acuario"
    print("Su signo es ", signo)
elif ((mes==2) and (dia>=20)) or ((mes==3) and (dia<=20)):
    signo = "Piscis"
    print("Su signo es ", signo)     
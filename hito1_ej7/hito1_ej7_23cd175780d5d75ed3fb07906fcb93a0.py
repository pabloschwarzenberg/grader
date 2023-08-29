#Horoscopo
dia=int(input("Ingrese el día de nacimiento: "))
mes=int(input("Ingrese el mes de nacimiento: "))

#Aries
if (mes==3 and dia>=21) or (mes==4 and dia<=20):
    print(" ARIES ")
#Tauro
elif (mes==4 and dia>20) or (mes==5 and dia<=21):
    print(" TAURO ")
#Geminis
elif (mes==5 and dia>21) or (mes==6 and dia<=21):
    print(" GEMINIS ")
#Cancer
elif (mes==6 and dia>21) or (mes==7 and dia<=23):
    print(" CANCER ")
#Leo
elif (mes==7 and dia>23) or (mes==8 and dia<=23):
    print(" LEO ")
#Virgo
elif (mes==8 and dia>23) or (mes==9 and dia<=23):
    print(" VIRGO ")
#Libra
elif (mes==9 and dia>23) or (mes==10 and dia<=23):
    print(" LIBRA ")
#Escorpion
elif (mes==10 and dia>23) or (mes==11 and dia<=22):
    print(" ESCORPION ")
#Sagitario
elif (mes==11 and dia>22) or (mes==12 and dia<=22):
    print(" SAGITARIO ")
#Capricornio
elif (mes==12 and dia>22) or (mes==1 and dia<=20):
    print(" CAPRICORNIO ")
#Acuario
elif (mes==1 and dia>20) or (mes==2 and dia<=19):
    print(" ACUARIO ")
#Piscis
elif (mes==2 and dia>19) or (mes==3 and dia<21):
    print(" TAURO ")    
print("Indicador de tu signo del zodiaco: ")
día = int(input("Escribir día de nacimiento: "))
mes = int(input("escribir mes de naciminto: "))
if ((mes==3) and(día>=21)) or ((mes==4)and(día<=20)):
    print("Aries: ")
elif ((mes==4) and(día>=21)) or ((mes==5) and(día<=20)):
    print("Tauro: ")
elif ((mes==5)and(día>=21)) or ((mes==6) and(día<=21)):
    print("Géminis: ")
elif ((mes==6) and(día>=22)) or ((mes==7) and(día<=21)):
    print("Cáncer: ")
elif ((mes==7) and(día>=22)) or ((mes==8) and(día<=23)):
    print("Leo: ")
elif ((mes==8) and(día>=24)) or ((mes==9) and(día<=22)):
    print("Virgo: ")
elif ((mes==9) and(día>=24)) or ((mes==10) and(día<=22)):
    print("Libra: ")
elif ((mes==10) and(día>=23)) or ((mes==11) and(día<=22)):
    print("Escorpio: ")
elif ((mes==11) and(día>=23)) or ((mes==12) and(día<=21)):
    print("Sagitario: ")
elif ((mes==12) and(día>=22)) or ((mes==1) and(día<=20)):
    print("Capricornio: ")
elif ((mes==1) and(día>=21)) or ((mes==2) and(día<=19)):
    print("Acuario: ")
elif ((mes==2) and(día>=20)) or ((mes==3) and(día<=20)):
    print("Piscis: ")
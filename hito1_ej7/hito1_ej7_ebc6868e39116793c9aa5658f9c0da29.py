#Zodiaco
D = int(input("Indique el día de tu cumpleaños: ")) 
M = int(input("Indique el mes de tu cumpleaños: "))
if ((M==3) and (D>=21)) or ((M==4) and (D<=20)):
    print("Tú signo del Zodiaco es: aries")
elif ((M==4) and (D>=20)) or ((M==5) and (D<=21)):
    print("Tú signo del Zodiaco es: Tauro")
elif ((M==5) and (D>=21)) or ((M==6) and (D<=21)):
    print("Tú signo del Zodiaco es: Géminis")
elif ((M==6) and (D>=21)) or ((M==7) and (D<=23)):
    print("Tú signo del Zodiaco es: Cáncer")
elif ((M==7) and (D>=23)) or ((M==8) and (D<=23)):
    print("Tú signo del Zodiaco es: Leo")
elif ((M==8) and (D>=23)) or ((M==9) and (D<=23)):
    print("Tú signo del Zodiaco es: Virgo")
elif ((M==9) and (D>=23)) or ((M==10) and (D<=23)):
    print("Tú signo del Zodiaco es: Libra")            
elif ((M==10) and (D>=23)) or ((M==11) and (D<=22)):
    print("Tú signo del Zodiaco es: Escorpio") 
elif ((M==11) and (D>=23)) or ((M==12) and (D<=22)):
    print("Tú signo del Zodiaco es: Sagitario") 
elif ((M==12) and (D>=22)) or ((M==1) and (D<=20)):
    print("Tú signo del Zodiaco es: Capricornio")
elif ((M==1) and (D>=20)) or ((M==2) and (D<=19)):
    print("Tú signo del Zodiaco es: Acuario")
elif ((M==2) and (D>=19)) or ((M==3) and (D<=21)):
    print("Tú signo del Zodiaco es: piscis")
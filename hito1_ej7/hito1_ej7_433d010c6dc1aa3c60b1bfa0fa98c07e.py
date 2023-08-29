#Zodiaco
día=int(input("¿Qué día naciste?\n"))
mes=int(input("¿Qué mes naciste? (En números)\n"))

while (día<=31 and mes<=12):
    if ((mes==3) and (día>=21)) or ((mes==4) and (día<=20)):
        print("Eres Aries")
        break
    elif ((mes==4) and (día>=20)) or ((mes==5) and (día<=21)):
        print("Eres Tauro")
        break
    elif ((mes==5) and (día>=21)) or ((mes==6) and (día<=21)):
        print("Eres Geminis")
        break
    elif ((mes==6) and (día>=21)) or ((mes==7) and (día<=23)):
        print("Eres Cancer")
        break
    elif ((mes==7) and (día>=23)) or ((mes==8) and (día<=23)):
        print("Eres Leo")
        break
    elif ((mes==8) and (día>=23)) or ((mes==9) and (día<=23)):
        print("Eres Virgo")
        break
    elif ((mes==9) and (día>=23)) or ((mes==10) and (día<=23)):
        print("Eres Libra")
        break
    elif ((mes==10) and (día>=23)) or ((mes==11) and (día<=22)):
        print("Eres Escorpio")
        break
    elif ((mes==11) and (día>=23)) or ((mes==12) and (día<=22)):
        print("Eres Sagitario")
        break
    elif ((mes==12) and (día>=22)) or ((mes==1) and (día<=20)):
        print("Eres Capricornio")
        break
    elif ((mes==1) and (día>=20)) or ((mes==2) and (día<=19)):
        print("Eres Aquario")
        break
    elif ((mes==2) and (día>=19)) or ((mes==3) and (día<=21)):
        print("Eres Piscis")
        break
else:
    print("Mes o día ingresados son invalidos \n")